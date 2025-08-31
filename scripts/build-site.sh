#!/bin/bash

# CS 5287 Cloud Computing - MkDocs Site Builder
# This script builds the complete documentation site from source materials

set -e  # Exit on error

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOC_SOURCE="$PROJECT_ROOT/doc"
DOCS_TARGET="$PROJECT_ROOT/docs"
SITE_OUTPUT="$PROJECT_ROOT/site"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."
    
    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        log_error "Python 3 is required but not installed"
        exit 1
    fi
    
    # Check if pip is available
    if ! command -v pip3 &> /dev/null; then
        log_error "pip3 is required but not installed"
        exit 1
    fi
    
    # Check if source directory exists
    if [[ ! -d "$DOC_SOURCE" ]]; then
        log_error "Source directory not found: $DOC_SOURCE"
        exit 1
    fi
    
    log_success "Prerequisites check passed"
}

# Install Python dependencies
install_dependencies() {
    log_info "Installing Python dependencies..."
    
    if [[ -f "$PROJECT_ROOT/requirements.txt" ]]; then
        pip3 install -r "$PROJECT_ROOT/requirements.txt"
        log_success "Dependencies installed"
    else
        log_warning "requirements.txt not found, skipping dependency installation"
    fi
}

# Clean previous build
clean_build() {
    log_info "Cleaning previous build..."
    
    if [[ -d "$SITE_OUTPUT" ]]; then
        rm -rf "$SITE_OUTPUT"
        log_info "Removed previous site output"
    fi
    
    # Clean and recreate docs directory structure
    if [[ -d "$DOCS_TARGET" ]]; then
        # Preserve assets directory if it exists
        if [[ -d "$DOCS_TARGET/assets" ]]; then
            mv "$DOCS_TARGET/assets" "/tmp/mkdocs_assets_backup" 2>/dev/null || true
        fi
        rm -rf "$DOCS_TARGET"
    fi
    
    mkdir -p "$DOCS_TARGET"
    
    # Restore assets if backup exists
    if [[ -d "/tmp/mkdocs_assets_backup" ]]; then
        mv "/tmp/mkdocs_assets_backup" "$DOCS_TARGET/assets"
        log_info "Restored assets directory"
    fi
    
    log_success "Build environment cleaned"
}

# Copy base content
copy_base_content() {
    log_info "Copying base content..."
    
    # Copy syllabus and schedule
    if [[ -f "$DOC_SOURCE/syllabus.md" ]]; then
        cp "$DOC_SOURCE/syllabus.md" "$DOCS_TARGET/"
        log_info "Copied syllabus.md"
    fi
    
    if [[ -f "$DOC_SOURCE/Schedule.md" ]]; then
        cp "$DOC_SOURCE/Schedule.md" "$DOCS_TARGET/schedule.md"
        log_info "Copied schedule.md"
    fi
    
    # Copy assignment documentation
    if [[ -d "$DOC_SOURCE/assignments" ]]; then
        cp -r "$DOC_SOURCE/assignments" "$DOCS_TARGET/"
        log_info "Copied assignments directory"
    fi
    
    log_success "Base content copied"
}

# Process Marp presentations
process_marp_files() {
    log_info "Processing Marp presentations..."
    
    python3 "$SCRIPT_DIR/convert-marp.py" "$DOC_SOURCE" "$DOCS_TARGET" --create-indexes
    
    if [[ $? -eq 0 ]]; then
        log_success "Marp files processed successfully"
    else
        log_error "Failed to process Marp files"
        exit 1
    fi
}

# Process PlantUML diagrams
process_plantuml_files() {
    log_info "Processing PlantUML diagrams..."
    
    python3 "$SCRIPT_DIR/process-plantuml.py" "$DOC_SOURCE" "$DOCS_TARGET" --validate --format svg
    
    if [[ $? -eq 0 ]]; then
        log_success "PlantUML files processed successfully"
    else
        log_warning "PlantUML processing had issues, but continuing..."
    fi
}

# Create home page
create_home_page() {
    log_info "Creating home page..."
    
    cat > "$DOCS_TARGET/index.md" << 'EOF'
# CS 5287 - Cloud Computing

<div class="course-header">
    <h2>Vanderbilt University - School of Engineering</h2>
    <p><strong>Instructor:</strong> Dr. Darren Pulsipher</p>
    <p><strong>Semester:</strong> Fall 2025</p>
</div>

## Welcome

Welcome to the CS 5287 Cloud Computing course materials site. This course provides an in-depth understanding of **cloud computing concepts, architectures, and technologies** through hands-on learning and real-world applications.

## Quick Navigation

<div class="week-nav">
    <div class="week-card">
        <h3>📚 Course Information</h3>
        <ul class="week-topics">
            <li><a href="syllabus/">Course Syllabus</a></li>
            <li><a href="schedule/">Assignment Schedule</a></li>
        </ul>
    </div>
    
    <div class="week-card">
        <h3>📝 Assignments</h3>
        <ul class="week-topics">
            <li><a href="assignments/">Assignment Overview</a></li>
            <li><a href="assignments/ca0/">CA0 - Manual Deployment</a></li>
            <li><a href="assignments/ca1/">CA1 - Infrastructure as Code</a></li>
            <li><a href="assignments/ca2/">CA2 - PaaS Orchestration</a></li>
            <li><a href="assignments/ca3/">CA3 - Cloud-Native Ops</a></li>
            <li><a href="assignments/ca4/">CA4 - Multi-Hybrid Cloud</a></li>
        </ul>
    </div>
    
    <div class="week-card">
        <h3>🎓 Weekly Content</h3>
        <ul class="week-topics">
            <li><a href="weeks/week-01/">Week 1 - Cloud Fundamentals</a></li>
            <li><a href="weeks/week-02/">Week 2 - Systems & Networking</a></li>
            <li><a href="weeks/week-03/">Week 3 - Virtualization & IaC</a></li>
            <li><a href="weeks/week-04/">Week 4 - Containers</a></li>
            <li><a href="weeks/week-05/">Week 5 - Kubernetes</a></li>
            <li>... and more</li>
        </ul>
    </div>
</div>

## Course Overview

This course walks you through cloud computing from fundamentals to advanced topics:

!!! info "Course Structure"
    - **Before Class:** Watch videos, read materials, work on assignments
    - **During Class:** Discussions, breakout sessions, presentations
    - **After Class:** Complete assignments, prepare for next week

### Learning Path

```mermaid
graph LR
    A[Cloud Fundamentals] --> B[Infrastructure]
    B --> C[Containers & Orchestration]
    C --> D[Advanced Topics]
    D --> E[Real-world Projects]
```

## Recent Updates

- ✅ Course site launched with all materials
- ✅ Week 1-4 content available
- 🔄 Assignment CA0 released
- 📅 See [schedule](schedule/) for upcoming deadlines

## Getting Help

- **Office Hours:** By appointment
- **Email:** [darren.pulsipher@vanderbilt.edu](mailto:darren.pulsipher@vanderbilt.edu)
- **Course Repository:** [GitHub](https://github.com/your-username/CS5287-Cloud)

!!! tip "Using Generative AI"
    This course **requires** the use of GenAI tools for learning, creating, and presenting. 
    Always verify AI-generated content and disclose your AI usage in assignments.

---

*Last updated: $(date)*
EOF

    log_success "Home page created"
}

# Create assignment index
create_assignment_index() {
    log_info "Creating assignment index..."
    
    mkdir -p "$DOCS_TARGET/assignments"
    
    cat > "$DOCS_TARGET/assignments/index.md" << 'EOF'
# Course Assignments

This page provides an overview of all course assignments for CS 5287 Cloud Computing.

## Assignment Progression

The assignments follow a logical progression through cloud computing modalities:

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA0</span>
        <h3>Manual Deployment</h3>
    </div>
    <p>Build and verify the full IoT pipeline "by hand" on cloud VMs. Learn each component end-to-end.</p>
    <p><strong>Due:</strong> September 5, 2025</p>
    <p><a href="ca0/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA1</span>
        <h3>Infrastructure as Code</h3>
    </div>
    <p>Recreate CA0 using automation tools like Ansible and Terraform.</p>
    <p><strong>Due:</strong> September 19, 2025</p>
    <p><a href="ca1/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA2</span>
        <h3>PaaS Orchestration</h3>
    </div>
    <p>Run the pipeline on Kubernetes or Docker Swarm using declarative manifests.</p>
    <p><strong>Due:</strong> October 17, 2025</p>
    <p><a href="ca2/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA3</span>
        <h3>Cloud-Native Ops</h3>
    </div>
    <p>Add observability, autoscaling, security hardening, and resilience testing.</p>
    <p><strong>Due:</strong> November 7, 2025</p>
    <p><a href="ca3/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA4</span>
        <h3>Multi-Hybrid Cloud (Final)</h3>
    </div>
    <p>Distribute components across sites/clouds with secure connectivity and failover.</p>
    <p><strong>Due:</strong> December 5, 2025</p>
    <p><a href="ca4/">→ View Details</a></p>
</div>

## Grading Rubric

All assignments are evaluated on:

| Category | Weight | Description |
|----------|--------|-------------|
| Correctness & Completeness | 15% | All components working end-to-end |
| Cloud-Model Execution | 25% | Proper use of cloud modality |
| Security | 15% | Security controls and best practices |
| Automation & Reproducibility | 10% | Clear, repeatable processes |
| Documentation & Diagrams | 30% | Comprehensive documentation |
| Demo Quality | 5% | Clear demonstration of working system |

## Reference Stack

Students should maintain the same logical architecture throughout all assignments:

- **Producers** → **Kafka Pub/Sub Hub** → **Processor** → **DB/Analytics**

Example components:
- **Kafka**: `bitnami/kafka:3.5.0`
- **Database**: `mongo:6.0.4` or `couchdb`
- **Processor**: Custom inference/transform service
- **Producers**: Data simulator containers

## Submission Requirements

Each assignment must be submitted to your GitHub repository:

```
github.com/your-username/CS5287/
├── CA0/README.md
├── CA1/README.md
├── CA2/README.md
├── CA3/README.md
└── CA4/README.md
```

!!! warning "Important"
    - Assignments are due at **11:59 PM CT** on the specified date
    - **No late submissions** will be accepted
    - Use GenAI responsibly and document its usage
EOF

    log_success "Assignment index created"
}

# Build MkDocs site
build_mkdocs_site() {
    log_info "Building MkDocs site..."
    
    cd "$PROJECT_ROOT"
    
    # Check if mkdocs.yml exists
    if [[ ! -f "mkdocs.yml" ]]; then
        log_error "mkdocs.yml not found in project root"
        exit 1
    fi
    
    # Build the site
    mkdocs build --clean
    
    if [[ $? -eq 0 ]]; then
        log_success "MkDocs site built successfully"
    else
        log_error "Failed to build MkDocs site"
        exit 1
    fi
}

# Serve site locally (optional)
serve_site() {
    if [[ "$1" == "--serve" ]]; then
        log_info "Starting local development server..."
        log_info "Site will be available at: http://127.0.0.1:8000"
        log_info "Press Ctrl+C to stop the server"
        
        cd "$PROJECT_ROOT"
        mkdocs serve
    fi
}

# Validate build
validate_build() {
    log_info "Validating build..."
    
    # Check if site directory was created
    if [[ ! -d "$SITE_OUTPUT" ]]; then
        log_error "Site output directory not found"
        exit 1
    fi
    
    # Check for essential files
    essential_files=("index.html" "syllabus/index.html" "assignments/index.html")
    
    for file in "${essential_files[@]}"; do
        if [[ ! -f "$SITE_OUTPUT/$file" ]]; then
            log_warning "Essential file missing: $file"
        fi
    done
    
    # Get site size
    site_size=$(du -sh "$SITE_OUTPUT" | cut -f1)
    log_info "Generated site size: $site_size"
    
    log_success "Build validation completed"
}

# Print usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --serve     Start local development server after build"
    echo "  --clean     Clean build only (no content processing)"
    echo "  --help      Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                # Full build"
    echo "  $0 --serve        # Build and serve locally"
    echo "  $0 --clean        # Clean build without processing"
}

# Main execution
main() {
    log_info "Starting CS 5287 documentation site build..."
    log_info "Project root: $PROJECT_ROOT"
    
    # Parse arguments
    SERVE_AFTER_BUILD=false
    CLEAN_ONLY=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            --serve)
                SERVE_AFTER_BUILD=true
                shift
                ;;
            --clean)
                CLEAN_ONLY=true
                shift
                ;;
            --help)
                usage
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                usage
                exit 1
                ;;
        esac
    done
    
    # Execute build steps
    check_prerequisites
    install_dependencies
    clean_build
    
    if [[ "$CLEAN_ONLY" == false ]]; then
        copy_base_content
        create_home_page
        create_assignment_index
        process_marp_files
        process_plantuml_files
    fi
    
    build_mkdocs_site
    validate_build
    
    log_success "Documentation site build completed!"
    log_info "Site location: $SITE_OUTPUT"
    
    if [[ "$SERVE_AFTER_BUILD" == true ]]; then
        serve_site --serve
    fi
}

# Run main function
main "$@"