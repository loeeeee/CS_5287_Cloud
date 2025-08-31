# MkDocs Static Documentation Site Design for CS 5287 Cloud Computing

## Overview

This document outlines the complete design for creating a static documentation site using MkDocs for the CS 5287 Cloud Computing course repository. The site will handle regular markdown, Marp presentations, PlantUML diagrams, and maintain the academic course structure.

## Project Structure

```
CS_5287_Cloud/
├── mkdocs.yml                 # Main MkDocs configuration
├── requirements.txt           # Python dependencies
├── docs/                      # MkDocs source directory
│   ├── index.md              # Home page
│   ├── syllabus.md           # Course syllabus
│   ├── schedule.md           # Course schedule
│   ├── assets/               # Shared assets
│   │   ├── css/
│   │   └── images/
│   ├── assignments/          # Assignment documentation
│   │   ├── index.md
│   │   ├── ca0.md
│   │   ├── ca1.md
│   │   ├── ca2.md
│   │   ├── ca3.md
│   │   └── ca4.md
│   └── weeks/                # Weekly content
│       ├── week-01/
│       ├── week-02/
│       └── ...
├── scripts/                  # Build and conversion scripts
│   ├── convert-marp.py       # Convert Marp to markdown
│   ├── process-plantuml.py   # Process PlantUML diagrams
│   └── build-site.sh         # Main build script
└── site/                     # Generated static site
```

## MkDocs Configuration (mkdocs.yml)

```yaml
site_name: CS 5287 - Cloud Computing
site_description: Vanderbilt University Cloud Computing Course Materials
site_author: Dr. Darren Pulsipher
site_url: https://your-domain.com/cs5287

repo_name: CS5287-Cloud
repo_url: https://github.com/your-username/CS5287-Cloud

theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: amber
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: amber
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
    - search.share
    - content.code.copy
    - content.action.edit

plugins:
  - search
  - plantuml:
      puml_url: https://www.plantuml.com/plantuml/
      num_workers: 8
  - awesome-pages
  - pdf-export:
      verbose: true
      media_type: print
      enabled_if_env: ENABLE_PDF_EXPORT

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - admonition
  - pymdownx.details
  - attr_list
  - md_in_html
  - tables
  - footnotes
  - def_list

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/your-username/CS5287-Cloud

nav:
  - Home: index.md
  - Course Information:
    - Syllabus: syllabus.md
    - Schedule: schedule.md
  - Assignments:
    - Overview: assignments/index.md
    - CA0 - Manual Deployment: assignments/ca0.md
    - CA1 - Infrastructure as Code: assignments/ca1.md
    - CA2 - PaaS Orchestration: assignments/ca2.md
    - CA3 - Cloud-Native Ops: assignments/ca3.md
    - CA4 - Multi-Hybrid Cloud: assignments/ca4.md
  - Weekly Content:
    - Week 1 - Cloud Computing Fundamentals: weeks/week-01/
    - Week 2 - Systems & Networking: weeks/week-02/
    - Week 3 - Virtualization & IaC: weeks/week-03/
    - Week 4 - Containers: weeks/week-04/
    - Week 5 - Kubernetes & Networking: weeks/week-05/
    - Week 6 - Scaling & Scheduling: weeks/week-06/
    - Week 7 - Tail Latencies: weeks/week-07/
    - Week 8 - Reliability & Chaos Engineering: weeks/week-08/
    - Week 9 - Serverless & Edge: weeks/week-09/
    - Week 10 - Cloud Storage: weeks/week-10/
    - Week 11 - Data Processing: weeks/week-11/
    - Week 12 - AI in the Cloud: weeks/week-12/
    - Week 13 - Networking Innovations: weeks/week-13/
    - Week 14 - Final Projects: weeks/week-14/
    - Week 15 - Presentations: weeks/week-15/
    - Week 16 - Wrap-up: weeks/week-16/
```

## Required Dependencies (requirements.txt)

```
mkdocs>=1.5.0
mkdocs-material>=9.0.0
mkdocs-plantuml>=1.0.0
mkdocs-awesome-pages-plugin>=2.8.0
mkdocs-pdf-export-plugin>=0.5.0
pymdown-extensions>=10.0.0
Pillow>=9.0.0
```

## Content Processing Strategy

### 1. Marp Presentation Handling

Since MkDocs doesn't natively support Marp presentations, we need to:

1. **Convert Marp to Standard Markdown**: Remove Marp frontmatter and convert slides to sections
2. **Preserve Slide Structure**: Use horizontal rules (`---`) to separate slides
3. **Add Navigation**: Create table of contents for each presentation
4. **Style Adaptations**: Use admonitions and special CSS for slide-like appearance

### 2. PlantUML Diagram Processing

Using the `mkdocs-plantuml` plugin:
1. **Automatic Rendering**: PlantUML files will be automatically rendered as SVG/PNG images
2. **Caching**: Diagrams are cached for faster builds
3. **Integration**: Diagrams can be referenced directly in markdown files

### 3. Directory Mapping

| Source Directory | Target Directory | Processing |
|-----------------|------------------|------------|
| `doc/syllabus.md` | `docs/syllabus.md` | Direct copy with path fixes |
| `doc/Schedule.md` | `docs/schedule.md` | Direct copy with path fixes |
| `doc/assignments/` | `docs/assignments/` | Restructure and process |
| `doc/Week X/` | `docs/weeks/week-XX/` | Convert Marp, process PlantUML |

## Build Process Scripts

### 1. Marp Conversion Script (convert-marp.py)

```python
# Converts Marp presentations to MkDocs-compatible markdown
# - Removes Marp frontmatter
# - Converts slides to sections
# - Fixes image paths
# - Adds navigation
```

### 2. PlantUML Processing Script (process-plantuml.py)

```python
# Processes PlantUML files
# - Validates PlantUML syntax
# - Generates image references
# - Updates markdown files with image links
```

### 3. Main Build Script (build-site.sh)

```bash
#!/bin/bash
# Main build script that:
# 1. Cleans previous build
# 2. Processes Marp files
# 3. Handles PlantUML diagrams
# 4. Copies assets
# 5. Builds MkDocs site
# 6. Optionally serves locally
```

## Styling and Theme Customization

### Custom CSS for Academic Content

```css
/* Slide-like styling for converted Marp content */
.slide-content {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
    background: #f9f9f9;
}

/* Assignment styling */
.assignment {
    border-left: 4px solid #2196F3;
    padding-left: 16px;
}

/* Week navigation */
.week-nav {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 20px 0;
}
```

## Content Organization Strategy

### Home Page Structure

```markdown
# CS 5287 - Cloud Computing

Welcome to the CS 5287 Cloud Computing course materials site.

## Quick Navigation

- [Course Syllabus](syllabus.md)
- [Assignment Schedule](schedule.md)
- [Weekly Content](weeks/)
- [Assignments](assignments/)

## Course Overview

This course provides an in-depth understanding of cloud computing concepts...

## Recent Updates

- Week 1 materials updated
- Assignment CA0 released
- Syllabus finalized
```

### Weekly Content Structure

Each week will have:
- Overview page with learning objectives
- Individual pages for each topic/presentation
- Links to related assignments
- Additional resources and readings

### Assignment Pages

Each assignment will include:
- Clear objectives and requirements
- Step-by-step instructions
- Grading rubric
- Example submissions
- FAQ section

## Deployment Options

1. **GitHub Pages**: Simple, free hosting with GitHub Actions for automated builds
2. **Netlify**: Automatic deployments with build previews
3. **Self-hosted**: On university servers or cloud providers
4. **Local**: For development and testing

## Performance Optimizations

1. **Image Optimization**: Compress images and use appropriate formats
2. **PlantUML Caching**: Cache rendered diagrams to speed up builds
3. **Lazy Loading**: Implement lazy loading for images and diagrams
4. **CDN**: Use CDN for faster asset delivery

## Maintenance and Updates

1. **Automated Builds**: Set up CI/CD pipeline for automatic site updates
2. **Content Validation**: Scripts to validate links and references
3. **Backup Strategy**: Regular backups of processed content
4. **Version Control**: Track changes and maintain history

## Implementation Timeline

1. **Phase 1**: Basic MkDocs setup with material theme
2. **Phase 2**: Content processing scripts (Marp, PlantUML)
3. **Phase 3**: Complete content migration and organization
4. **Phase 4**: Custom styling and optimization
5. **Phase 5**: Deployment and testing