#!/usr/bin/env python3
"""
Marp to MkDocs Converter
Converts Marp presentation files (.marp.md) to MkDocs-compatible markdown files.
"""

import os
import re
import yaml
import argparse
from pathlib import Path
import shutil


class MarpConverter:
    def __init__(self, source_dir, target_dir):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.target_dir.mkdir(parents=True, exist_ok=True)
    
    def convert_file(self, marp_file):
        """Convert a single Marp file to MkDocs format."""
        print(f"Converting: {marp_file}")
        
        with open(marp_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter, body = self.extract_frontmatter(content)
        
        # Process the body content
        converted_body = self.process_marp_content(body, frontmatter)
        
        # Generate output filename
        output_file = self.get_output_filename(marp_file)
        
        # Write converted content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_body)
        
        print(f"Converted to: {output_file}")
        return output_file
    
    def extract_frontmatter(self, content):
        """Extract YAML frontmatter from Marp file."""
        frontmatter = {}
        body = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    body = parts[2].strip()
                except yaml.YAMLError:
                    print("Warning: Could not parse frontmatter")
        
        return frontmatter, body
    
    def process_marp_content(self, body, frontmatter):
        """Convert Marp-specific content to MkDocs format."""
        # Start with title from frontmatter if available
        title = frontmatter.get('title', 'Presentation')
        description = frontmatter.get('description', '')
        
        # Create header
        converted = f"# {title}\n\n"
        if description:
            converted += f"{description}\n\n"
        
        # Add presentation info
        if frontmatter.get('marp'):
            converted += '!!! info "Presentation Format"\n'
            converted += '    This content was originally created as a Marp presentation.\n\n'
        
        # Split content by slide separators
        slides = re.split(r'^---\s*$', body, flags=re.MULTILINE)
        
        # Process each slide
        for i, slide in enumerate(slides):
            if slide.strip():
                converted += self.process_slide(slide.strip(), i + 1)
        
        return converted
    
    def process_slide(self, slide_content, slide_number):
        """Process individual slide content."""
        lines = slide_content.split('\n')
        processed_lines = []
        
        # Wrap slide in a container
        processed_lines.append(f'<div class="slide-content" id="slide-{slide_number}">')
        processed_lines.append('')
        
        for line in lines:
            # Process Marp-specific syntax
            line = self.process_marp_syntax(line)
            processed_lines.append(line)
        
        processed_lines.append('')
        processed_lines.append('</div>')
        processed_lines.append('')
        
        return '\n'.join(processed_lines)
    
    def process_marp_syntax(self, line):
        """Process Marp-specific syntax and convert to standard markdown."""
        # Remove Marp-specific comments
        if line.strip().startswith('<!--'):
            return ''
        
        # Convert Marp image syntax with positioning
        line = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)\s*{[^}]*}', r'![\1](\2)', line)
        
        # Process background directives (convert to admonitions)
        if '<!-- _backgroundColor:' in line or '<!-- _color:' in line:
            return ''
        
        # Fix relative image paths
        line = self.fix_image_paths(line)
        
        return line
    
    def fix_image_paths(self, line):
        """Fix relative image paths for MkDocs structure."""
        # Pattern to match markdown images
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        def replace_path(match):
            alt_text = match.group(1)
            img_path = match.group(2)
            
            # Skip absolute URLs
            if img_path.startswith(('http://', 'https://')):
                return match.group(0)
            
            # Convert relative paths
            if not img_path.startswith('/'):
                # Assume images are in the same directory or subdirectory
                img_path = f"../assets/images/{os.path.basename(img_path)}"
            
            return f'![{alt_text}]({img_path})'
        
        return re.sub(img_pattern, replace_path, line)
    
    def get_output_filename(self, marp_file):
        """Generate output filename for converted file."""
        marp_file = Path(marp_file)
        
        # Remove .marp from the filename
        name = marp_file.stem
        if name.endswith('.marp'):
            name = name[:-5]
        
        # Create target directory structure
        relative_path = marp_file.parent.relative_to(self.source_dir)
        target_dir = self.target_dir / relative_path
        target_dir.mkdir(parents=True, exist_ok=True)
        
        return target_dir / f"{name}.md"
    
    def copy_assets(self):
        """Copy image and other assets to the docs directory."""
        assets_copied = 0
        
        for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg']:
            for asset_file in self.source_dir.rglob(ext):
                # Copy to docs/assets/images/
                target_file = self.target_dir / 'assets' / 'images' / asset_file.name
                target_file.parent.mkdir(parents=True, exist_ok=True)
                
                if not target_file.exists() or asset_file.stat().st_mtime > target_file.stat().st_mtime:
                    shutil.copy2(asset_file, target_file)
                    assets_copied += 1
        
        print(f"Copied {assets_copied} asset files")
    
    def convert_all(self):
        """Convert all Marp files in the source directory."""
        marp_files = list(self.source_dir.rglob('*.marp.md'))
        
        if not marp_files:
            print("No Marp files found")
            return
        
        print(f"Found {len(marp_files)} Marp files to convert")
        
        converted_files = []
        for marp_file in marp_files:
            try:
                output_file = self.convert_file(marp_file)
                converted_files.append(output_file)
            except Exception as e:
                print(f"Error converting {marp_file}: {e}")
        
        # Copy assets
        self.copy_assets()
        
        print(f"\nConversion complete. {len(converted_files)} files converted.")
        return converted_files


def create_week_index(week_dir, week_number):
    """Create an index file for a week directory."""
    index_file = week_dir / 'index.md'
    
    # Find all markdown files in the week directory
    md_files = [f for f in week_dir.glob('*.md') if f.name != 'index.md']
    
    content = f"""# Week {week_number}

## Topics This Week

"""
    
    for md_file in sorted(md_files):
        title = md_file.stem.replace('_', ' ').title()
        content += f"- [{title}]({md_file.name})\n"
    
    content += """
## Learning Objectives

After this week, you should be able to:

- Understand the key concepts covered in this week's materials
- Apply the techniques and tools discussed
- Complete the related assignments and exercises

## Additional Resources

- Course readings and references
- External documentation and tutorials
- Practice exercises and examples
"""
    
    with open(index_file, 'w') as f:
        f.write(content)
    
    print(f"Created week index: {index_file}")


def main():
    parser = argparse.ArgumentParser(description='Convert Marp presentations to MkDocs format')
    parser.add_argument('source', help='Source directory containing Marp files')
    parser.add_argument('target', help='Target docs directory')
    parser.add_argument('--create-indexes', action='store_true', 
                       help='Create index files for week directories')
    
    args = parser.parse_args()
    
    converter = MarpConverter(args.source, args.target)
    converted_files = converter.convert_all()
    
    if args.create_indexes:
        # Create week index files
        weeks_dir = Path(args.target) / 'weeks'
        if weeks_dir.exists():
            for week_dir in sorted(weeks_dir.iterdir()):
                if week_dir.is_dir() and week_dir.name.startswith('week-'):
                    week_num = week_dir.name.split('-')[1]
                    create_week_index(week_dir, week_num)


if __name__ == '__main__':
    main()