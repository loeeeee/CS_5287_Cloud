// CS 5287 Cloud Computing Course - Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize custom functionality
    initializeWeekNavigation();
    initializeSlideContent();
    initializeAssignmentTracking();
    initializeVideoEmbeds();
    
    console.log('CS 5287 Course site initialized');
});

/**
 * Initialize week navigation enhancements
 */
function initializeWeekNavigation() {
    const weekCards = document.querySelectorAll('.week-card');
    
    weekCards.forEach(card => {
        // Add click functionality to week cards
        card.addEventListener('click', function() {
            const link = card.querySelector('a');
            if (link) {
                window.location.href = link.href;
            }
        });
        
        // Add hover effects
        card.addEventListener('mouseenter', function() {
            this.style.cursor = 'pointer';
        });
    });
}

/**
 * Initialize slide content functionality
 */
function initializeSlideContent() {
    const slideContents = document.querySelectorAll('.slide-content');
    
    slideContents.forEach((slide, index) => {
        // Add slide numbering
        const slideNumber = document.createElement('div');
        slideNumber.className = 'slide-number';
        slideNumber.textContent = `Slide ${index + 1}`;
        slideNumber.style.cssText = `
            position: absolute;
            top: 8px;
            left: 12px;
            font-size: 0.8em;
            color: #666;
            font-weight: bold;
        `;
        slide.appendChild(slideNumber);
        
        // Add expand/collapse functionality for long slides
        if (slide.scrollHeight > 600) {
            addExpandCollapseButton(slide);
        }
    });
}

/**
 * Add expand/collapse functionality to long slides
 */
function addExpandCollapseButton(slide) {
    const button = document.createElement('button');
    button.textContent = 'Expand';
    button.className = 'slide-expand-btn';
    button.style.cssText = `
        position: absolute;
        bottom: 8px;
        right: 8px;
        background: var(--vu-blue);
        color: white;
        border: none;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8em;
        cursor: pointer;
    `;
    
    let isExpanded = false;
    slide.style.maxHeight = '400px';
    slide.style.overflow = 'hidden';
    
    button.addEventListener('click', function() {
        if (isExpanded) {
            slide.style.maxHeight = '400px';
            button.textContent = 'Expand';
        } else {
            slide.style.maxHeight = 'none';
            button.textContent = 'Collapse';
        }
        isExpanded = !isExpanded;
    });
    
    slide.appendChild(button);
}

/**
 * Initialize assignment tracking functionality
 */
function initializeAssignmentTracking() {
    const assignments = document.querySelectorAll('.assignment');
    
    assignments.forEach(assignment => {
        // Check for due dates and add visual indicators
        const dueDateElement = assignment.querySelector('.due-date');
        if (dueDateElement) {
            const dueDate = new Date(dueDateElement.textContent);
            const now = new Date();
            const timeDiff = dueDate - now;
            const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
            
            // Add urgency indicators
            if (daysDiff < 0) {
                assignment.classList.add('past-due');
            } else if (daysDiff <= 3) {
                assignment.classList.add('due-soon');
            } else if (daysDiff <= 7) {
                assignment.classList.add('due-this-week');
            }
            
            // Add countdown
            if (daysDiff > 0) {
                const countdown = document.createElement('div');
                countdown.className = 'assignment-countdown';
                countdown.textContent = `${daysDiff} days remaining`;
                countdown.style.cssText = `
                    font-size: 0.9em;
                    color: #666;
                    font-style: italic;
                    margin-top: 8px;
                `;
                assignment.appendChild(countdown);
            }
        }
    });
}

/**
 * Initialize video embed functionality
 */
function initializeVideoEmbeds() {
    // Convert YouTube links to embeds
    const videoLinks = document.querySelectorAll('a[href*="youtube.com"], a[href*="youtu.be"]');
    
    videoLinks.forEach(link => {
        const href = link.href;
        let videoId = '';
        
        // Extract video ID from various YouTube URL formats
        if (href.includes('youtube.com/watch?v=')) {
            videoId = href.split('v=')[1].split('&')[0];
        } else if (href.includes('youtu.be/')) {
            videoId = href.split('youtu.be/')[1].split('?')[0];
        }
        
        if (videoId) {
            // Create embed container
            const container = document.createElement('div');
            container.className = 'video-container';
            
            const iframe = document.createElement('iframe');
            iframe.src = `https://www.youtube.com/embed/${videoId}`;
            iframe.setAttribute('allowfullscreen', '');
            iframe.setAttribute('frameborder', '0');
            
            container.appendChild(iframe);
            
            // Replace link with embed (optional - could be behind a click)
            const embedButton = document.createElement('button');
            embedButton.textContent = '▶ Watch Video';
            embedButton.className = 'video-embed-btn';
            embedButton.style.cssText = `
                background: #ff0000;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                cursor: pointer;
                margin: 8px 0;
            `;
            
            embedButton.addEventListener('click', function() {
                this.parentNode.replaceChild(container, this);
            });
            
            link.parentNode.insertBefore(embedButton, link.nextSibling);
        }
    });
}

/**
 * Add search functionality for course content
 */
function initializeCourseSearch() {
    // Enhanced search for course-specific content
    const searchInput = document.querySelector('[data-md-component="search-query"]');
    
    if (searchInput) {
        // Add course-specific search suggestions
        const suggestions = [
            'assignments', 'syllabus', 'schedule', 'docker', 'kubernetes',
            'cloud computing', 'virtualization', 'containers', 'REST',
            'kafka', 'microservices', 'scaling', 'load balancing'
        ];
        
        // Could implement autocomplete here
        console.log('Search suggestions available:', suggestions);
    }
}

/**
 * Add print functionality for individual pages
 */
function addPrintFunctionality() {
    const printButton = document.createElement('button');
    printButton.innerHTML = '🖨️ Print Page';
    printButton.className = 'print-btn';
    printButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: var(--vu-blue);
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 25px;
        cursor: pointer;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    `;
    
    printButton.addEventListener('click', function() {
        window.print();
    });
    
    document.body.appendChild(printButton);
}

/**
 * Initialize theme enhancements
 */
function initializeThemeEnhancements() {
    // Add Vanderbilt branding elements
    const header = document.querySelector('.md-header');
    if (header) {
        // Could add university logo or additional branding here
        console.log('Header found for branding');
    }
    
    // Add course-specific color scheme handling
    const colorSchemeToggle = document.querySelector('[data-md-color-scheme]');
    if (colorSchemeToggle) {
        console.log('Color scheme toggle available');
    }
}

// Add CSS for dynamic elements
const style = document.createElement('style');
style.textContent = `
    .assignment.past-due {
        border-left-color: #dc3545;
        background: linear-gradient(90deg, rgba(220, 53, 69, 0.1) 0%, transparent 100%);
    }
    
    .assignment.due-soon {
        border-left-color: #fd7e14;
        background: linear-gradient(90deg, rgba(253, 126, 20, 0.1) 0%, transparent 100%);
    }
    
    .assignment.due-this-week {
        border-left-color: #ffc107;
        background: linear-gradient(90deg, rgba(255, 193, 7, 0.1) 0%, transparent 100%);
    }
    
    .slide-expand-btn:hover {
        background: #041E42 !important;
    }
    
    .video-embed-btn:hover {
        background: #cc0000 !important;
    }
    
    .print-btn:hover {
        transform: scale(1.05);
    }
`;

document.head.appendChild(style);

// Initialize additional functionality when needed
window.addEventListener('load', function() {
    initializeCourseSearch();
    addPrintFunctionality();
    initializeThemeEnhancements();
});