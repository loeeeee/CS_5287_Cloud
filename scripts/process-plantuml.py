#!/usr/bin/env python3
"""
PlantUML Processor for MkDocs
Processes PlantUML files and updates markdown references.
"""

import os
import re
import argparse
import requests
import base64
import zlib
from pathlib import Path
import shutil


class PlantUMLProcessor:
    def __init__(self, source_dir, docs_dir):
        self.source_dir = Path(source_dir)
        self.docs_dir = Path(docs_dir)
        self.images_dir = self.docs_dir / 'assets' / 'images' / 'diagrams'
        self.images_dir.mkdir(parents=True, exist_ok=True)
        
        # PlantUML server URL (can be changed to local installation)
        self.plantuml_server = "https://www.plantuml.com/plantuml"
    
    def encode_plantuml(self, plantuml_text):
        """Encode PlantUML text for URL."""
        plantuml_text = plantuml_text.encode('utf-8')
        compressed = zlib.compress(plantuml_text)
        encoded = base64.b64encode(compressed).decode('ascii')
        # Convert to PlantUML's URL-safe encoding
        encoded = encoded.translate(str.maketrans('+/', '-_'))
        return encoded.rstrip('=')
    
    def generate_diagram_image(self, puml_file, format='svg'):
        """Generate diagram image from PlantUML file."""
        try:
            with open(puml_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove @startuml/@enduml if present (they'll be added by server)
            content = re.sub(r'@startuml.*?\n', '', content)
            content = re.sub(r'@enduml.*?\n?', '', content)
            
            # Encode for PlantUML server
            encoded = self.encode_plantuml(f"@startuml\n{content}\n@enduml")
            
            # Request image from PlantUML server
            url = f"{self.plantuml_server}/{format}/{encoded}"
            response = requests.get(url, timeout=30)
            
            if response.status_code == 200:
                # Save image
                image_name = f"{puml_file.stem}.{format}"
                image_path = self.images_dir / image_name
                
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                
                print(f"Generated diagram: {image_path}")
                return image_path
            else:
                print(f"Failed to generate diagram for {puml_file}: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error processing {puml_file}: {e}")
            return None
    
    def process_all_plantuml_files(self):
        """Process all PlantUML files in the source directory."""
        puml_files = list(self.source_dir.rglob('*.puml'))
        
        if not puml_files:
            print("No PlantUML files found")
            return {}
        
        print(f"Found {len(puml_files)} PlantUML files to process")
        
        processed_files = {}
        
        for puml_file in puml_files:
            image_path = self.generate_diagram_image(puml_file)
            if image_path:
                # Store mapping for markdown updates
                relative_image_path = image_path.relative_to(self.docs_dir)
                processed_files[puml_file.name] = str(relative_image_path)
        
        print(f"Processed {len(processed_files)} PlantUML files")
        return processed_files
    
    def update_markdown_references(self, processed_files):
        """Update markdown files to reference generated images instead of .puml files."""
        if not processed_files:
            return
        
        md_files = list(self.docs_dir.rglob('*.md'))
        updated_files = 0
        
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace PlantUML references with image references
                for puml_name, image_path in processed_files.items():
                    # Pattern for markdown links to .puml files
                    puml_pattern = rf'\[([^\]]*)\]\({re.escape(puml_name)}\)'
                    image_replacement = f'![\\1]({image_path})'
                    content = re.sub(puml_pattern, image_replacement, content)
                    
                    # Pattern for direct .puml references
                    direct_pattern = rf'\b{re.escape(puml_name)}\b'
                    if re.search(direct_pattern, content):
                        content = re.sub(direct_pattern, f'![{puml_name.replace(".puml", "")}]({image_path})', content)
                
                # Write back if content changed
                if content != original_content:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated_files += 1
                    print(f"Updated references in: {md_file}")
                
            except Exception as e:
                print(f"Error updating {md_file}: {e}")
        
        print(f"Updated {updated_files} markdown files")
    
    def create_diagram_index(self, processed_files):
        """Create an index of all diagrams."""
        if not processed_files:
            return
        
        index_content = """# Architecture Diagrams

This page contains all the PlantUML diagrams used throughout the course.

"""
        
        for puml_name, image_path in sorted(processed_files.items()):
            diagram_name = puml_name.replace('.puml', '').replace('_', ' ').title()
            index_content += f"## {diagram_name}\n\n"
            index_content += f"![{diagram_name}]({image_path})\n\n"
            index_content += f"*Source: {puml_name}*\n\n"
            index_content += "---\n\n"
        
        index_file = self.docs_dir / 'diagrams.md'
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"Created diagram index: {index_file}")
    
    def copy_plantuml_source(self):
        """Copy PlantUML source files to docs for reference."""
        source_dir = self.docs_dir / 'assets' / 'plantuml'
        source_dir.mkdir(parents=True, exist_ok=True)
        
        puml_files = list(self.source_dir.rglob('*.puml'))
        copied = 0
        
        for puml_file in puml_files:
            target_file = source_dir / puml_file.name
            shutil.copy2(puml_file, target_file)
            copied += 1
        
        print(f"Copied {copied} PlantUML source files")


def validate_plantuml_syntax(puml_file):
    """Validate PlantUML syntax."""
    try:
        with open(puml_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic syntax validation
        if not content.strip():
            return False, "Empty file"
        
        # Check for required elements
        if '@startuml' not in content and '@startmindmap' not in content:
            return False, "Missing @startuml directive"
        
        if '@enduml' not in content and '@endmindmap' not in content:
            return False, "Missing @enduml directive"
        
        return True, "Valid"
        
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description='Process PlantUML files for MkDocs')
    parser.add_argument('source', help='Source directory containing PlantUML files')
    parser.add_argument('docs', help='Docs directory for generated images')
    parser.add_argument('--validate', action='store_true', 
                       help='Validate PlantUML syntax before processing')
    parser.add_argument('--format', choices=['svg', 'png'], default='svg',
                       help='Output format for diagrams')
    parser.add_argument('--server', default='https://www.plantuml.com/plantuml',
                       help='PlantUML server URL')
    
    args = parser.parse_args()
    
    processor = PlantUMLProcessor(args.source, args.docs)
    processor.plantuml_server = args.server
    
    # Validate files if requested
    if args.validate:
        print("Validating PlantUML files...")
        puml_files = list(Path(args.source).rglob('*.puml'))
        
        for puml_file in puml_files:
            is_valid, message = validate_plantuml_syntax(puml_file)
            status = "✓" if is_valid else "✗"
            print(f"{status} {puml_file}: {message}")
    
    # Process all PlantUML files
    processed_files = processor.process_all_plantuml_files()
    
    # Update markdown references
    processor.update_markdown_references(processed_files)
    
    # Create diagram index
    processor.create_diagram_index(processed_files)
    
    # Copy source files
    processor.copy_plantuml_source()
    
    print("PlantUML processing complete!")


if __name__ == '__main__':
    main()