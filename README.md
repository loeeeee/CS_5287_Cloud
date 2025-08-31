# CS 5287 Cloud Computing - Documentation Site

A comprehensive static documentation site for Vanderbilt University's CS 5287 Cloud Computing course, built with MkDocs and featuring automated processing of Marp presentations and PlantUML diagrams.

## 🎯 Features

- **📚 Complete Course Materials**: All lectures, assignments, and resources in one place
- **🎨 Professional Design**: Material theme with Vanderbilt University branding
- **📊 Interactive Diagrams**: Automatic PlantUML diagram rendering to SVG
- **🎪 Presentation Support**: Marp presentation files converted to accessible markdown
- **🔍 Advanced Search**: Full-text search across all course content
- **📱 Responsive Design**: Works on desktop, tablet, and mobile devices
- **🌙 Dark/Light Theme**: User preference toggle
- **🖨️ PDF Export**: Optional PDF generation for offline use

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - Required for MkDocs and processing scripts
- **Git** - For cloning and version control
- **Internet Connection** - For PlantUML diagram generation

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CS_5287_Cloud
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the documentation site:**
   ```bash
   ./scripts/build-site.sh
   ```

5. **Serve locally:**
   ```bash
   mkdocs serve
   # or
   ./scripts/build-site.sh --serve
   ```

The site will be available at `http://127.0.0.1:8000`

## 📁 Project Structure

```
CS_5287_Cloud/
├── doc/                          # Source course materials
│   ├── syllabus.md              # Course syllabus
│   ├── Schedule.md              # Course schedule
│   ├── assignments/             # Assignment specifications
│   └── Week X/                  # Weekly content and presentations
├── docs/                        # Processed documentation (generated)
│   ├── index.md                # Home page
│   ├── assets/                 # Styling and images
│   └── weeks/                  # Processed weekly content
├── scripts/                     # Build and processing scripts
│   ├── build-site.sh           # Main build script
│   ├── convert-marp.py         # Marp presentation converter
│   └── process-plantuml.py     # PlantUML diagram processor
├── site/                       # Generated static site
├── mkdocs.yml                  # MkDocs configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 Build Process

The documentation site uses a sophisticated build process that handles multiple content types:

### 1. Content Processing

**Marp Presentations** → **Standard Markdown**
- Removes Marp-specific frontmatter
- Converts slide separators to sections
- Preserves slide structure with custom styling
- Fixes image paths for MkDocs structure

**PlantUML Diagrams** → **SVG Images**
- Validates PlantUML syntax
- Generates SVG diagrams via PlantUML server
- Updates markdown references automatically
- Creates centralized diagram index

### 2. Site Generation

**MkDocs Build Process:**
- Applies Material theme with custom styling
- Processes markdown extensions and plugins
- Generates navigation structure
- Creates search index
- Outputs static HTML site

## 🛠️ Development

### Local Development Server

For development with auto-reload:

```bash
# Activate virtual environment
source venv/bin/activate

# Start development server
mkdocs serve --dev-addr 127.0.0.1:8000

# Or with full rebuild
./scripts/build-site.sh --serve
```

### Making Content Changes

#### Adding New Course Content

1. **Add materials to `doc/` directory** following existing structure
2. **Run the build script** to process new content:
   ```bash
   ./scripts/build-site.sh
   ```
3. **Update navigation** in `mkdocs.yml` if needed

#### Updating Existing Content

1. **Edit source files** in `doc/` directory
2. **Rebuild the site:**
   ```bash
   mkdocs build --clean
   ```

#### Working with Marp Presentations

Marp files should follow this structure:
```yaml
---
marp: true
theme: default
paginate: true
title: Your Presentation Title
---

# Slide 1 Content

---

# Slide 2 Content
```

#### Working with PlantUML Diagrams

PlantUML files should be valid PlantUML syntax:
```plantuml
@startuml
title Your Diagram Title

' Diagram content here

@enduml
```

### Custom Styling

The site uses custom CSS for course-specific styling:

- **Vanderbilt Branding**: Colors and fonts matching university standards
- **Slide Styling**: Special formatting for converted Marp content
- **Assignment Layout**: Structured display for course assignments
- **Responsive Design**: Mobile-friendly layouts

Custom styles are in:
- [`docs/assets/css/custom.css`](docs/assets/css/custom.css) - Main stylesheet
- [`docs/assets/js/custom.js`](docs/assets/js/custom.js) - Interactive features

## 🚀 Deployment Options

### 1. GitHub Pages

```bash
# Build and deploy to GitHub Pages
mkdocs gh-deploy
```

### 2. Netlify

1. Connect your repository to Netlify
2. Set build command: `./scripts/build-site.sh`
3. Set publish directory: `site/`
4. Enable automatic deployments

### 3. Self-Hosted

```bash
# Build static site
mkdocs build

# Deploy contents of site/ directory to web server
rsync -av site/ user@server:/var/www/html/
```

### 4. Docker Deployment

```dockerfile
FROM nginx:alpine
COPY site/ /usr/share/nginx/html/
EXPOSE 80
```

## 📊 Analytics and Monitoring

The site includes support for:

- **Google Analytics** - Configure in `mkdocs.yml`
- **Search Analytics** - Track popular content
- **Performance Monitoring** - Monitor load times
- **User Engagement** - Track navigation patterns

## 🔒 Configuration

### Environment Variables

```bash
# Enable PDF export
export ENABLE_PDF_EXPORT=1

# PlantUML server (optional)
export PLANTUML_SERVER=https://your-plantuml-server.com
```

### MkDocs Configuration

Key configuration sections in [`mkdocs.yml`](mkdocs.yml):

- **Site Information** - Title, description, URLs
- **Theme Configuration** - Material theme settings
- **Plugin Configuration** - Search, PDF export, etc.
- **Markdown Extensions** - Syntax highlighting, admonitions
- **Navigation Structure** - Course organization

## 🐛 Troubleshooting

### Common Issues

1. **Build Failures**
   ```bash
   # Clear cache and rebuild
   rm -rf site/ docs/
   ./scripts/build-site.sh
   ```

2. **Missing Dependencies**
   ```bash
   # Reinstall requirements
   pip install --force-reinstall -r requirements.txt
   ```

3. **PlantUML Errors**
   ```bash
   # Validate PlantUML files
   ./scripts/process-plantuml.py doc/ docs/ --validate
   ```

4. **Navigation Issues**
   - Check file paths in `mkdocs.yml`
   - Ensure all referenced files exist
   - Verify markdown file structure

### Debug Mode

Enable verbose output:
```bash
mkdocs build --verbose
mkdocs serve --verbose
```

### Log Analysis

Check build logs for:
- Missing files
- Broken links
- Plugin errors
- Content warnings

## 📈 Performance Optimization

### Build Performance

- **Parallel Processing** - PlantUML generation uses multiple workers
- **Caching** - Generated diagrams are cached
- **Incremental Builds** - Only changed content is processed

### Site Performance

- **Image Optimization** - SVG diagrams for scalability
- **Minification** - CSS and JS are minified
- **CDN Support** - Assets can be served via CDN
- **Lazy Loading** - Images load on demand

## 🤝 Contributing

### Content Contributions

1. Fork the repository
2. Add or update content in `doc/` directory
3. Test locally with `./scripts/build-site.sh --serve`
4. Submit pull request

### Code Contributions

1. Fork the repository
2. Create feature branch
3. Make changes to scripts or configuration
4. Test thoroughly
5. Submit pull request

### Reporting Issues

- Use GitHub Issues for bug reports
- Include build logs and environment details
- Provide steps to reproduce

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Course Information

**CS 5287 - Cloud Computing**  
**Vanderbilt University - School of Engineering**  
**Instructor:** Dr. Darren Pulsipher  
**Semester:** Fall 2025  

For course-specific questions, contact: [darren.pulsipher@vanderbilt.edu](mailto:darren.pulsipher@vanderbilt.edu)

## 🔗 Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Marp](https://marp.app/) - Markdown Presentation Ecosystem
- [PlantUML](https://plantuml.com/) - UML Diagram Tool
- [Vanderbilt University](https://www.vanderbilt.edu/)

---

**Built with ❤️ for CS 5287 students**
