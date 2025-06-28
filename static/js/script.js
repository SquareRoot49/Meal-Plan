// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }));
}

// Navbar background on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        }
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Flash message handling
function showFlashMessage(message, type = 'info') {
    // Remove existing flash messages
    const existingMessages = document.querySelectorAll('.flash-message');
    existingMessages.forEach(msg => msg.remove());

    // Create flash message element
    const flashMessage = document.createElement('div');
    flashMessage.className = `flash-message flash-${type}`;
    flashMessage.innerHTML = `
        <span>${message}</span>
        <button class="flash-close">&times;</button>
    `;

    // Add to flash messages container
    let flashContainer = document.querySelector('.flash-messages');
    if (!flashContainer) {
        flashContainer = document.createElement('div');
        flashContainer.className = 'flash-messages';
        document.body.appendChild(flashContainer);
    }

    flashContainer.appendChild(flashMessage);

    // Animate in
    setTimeout(() => {
        flashMessage.classList.add('show');
    }, 100);

    // Close button functionality
    const closeBtn = flashMessage.querySelector('.flash-close');
    closeBtn.addEventListener('click', () => {
        flashMessage.classList.remove('show');
        setTimeout(() => flashMessage.remove(), 300);
    });

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (flashMessage.parentNode) {
            flashMessage.classList.remove('show');
            setTimeout(() => flashMessage.remove(), 300);
        }
    }, 5000);
}

// Form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = '#ef4444';
            
            // Add error message
            let errorMsg = input.parentNode.querySelector('.error-message');
            if (!errorMsg) {
                errorMsg = document.createElement('div');
                errorMsg.className = 'error-message';
                errorMsg.style.color = '#ef4444';
                errorMsg.style.fontSize = '0.8rem';
                errorMsg.style.marginTop = '0.25rem';
                input.parentNode.appendChild(errorMsg);
            }
            errorMsg.textContent = 'This field is required';
        } else {
            input.style.borderColor = '#e5e7eb';
            const errorMsg = input.parentNode.querySelector('.error-message');
            if (errorMsg) {
                errorMsg.remove();
            }
        }
    });

    return isValid;
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Contact form handling
const contactForm = document.querySelector('form[action*="contact"]');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (!validateForm(this)) {
            showFlashMessage('Please fill in all required fields.', 'error');
            return;
        }

        const email = this.querySelector('input[type="email"]');
        if (email && !isValidEmail(email.value)) {
            showFlashMessage('Please enter a valid email address.', 'error');
            return;
        }

        // Simulate form submission
        showFlashMessage('Thank you for your message! We\'ll get back to you soon.', 'success');
        this.reset();
    });
}

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.feature-card, .step, .meal-section');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Button click animations
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        // Create ripple effect
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
        `;
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple animation CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translateY(${rate}px)`;
    }
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// Utility functions
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Search functionality for food database
const searchInput = document.querySelector('#searchFood');
if (searchInput) {
    const debouncedSearch = debounce(function(searchTerm) {
        const foodItems = document.querySelectorAll('.food-item');
        foodItems.forEach(item => {
            const foodName = item.querySelector('.food-name').textContent.toLowerCase();
            if (foodName.includes(searchTerm.toLowerCase())) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }, 300);

    searchInput.addEventListener('input', (e) => {
        debouncedSearch(e.target.value);
    });
}

// Filter functionality for food categories
const categoryFilters = document.querySelectorAll('.category-filter');
if (categoryFilters.length > 0) {
    categoryFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const category = this.dataset.category;
            const foodItems = document.querySelectorAll('.food-item');
            
            // Update active filter
            categoryFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');
            
            foodItems.forEach(item => {
                if (category === 'all' || item.dataset.category === category) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
}

// Save meal plan functionality
function saveMealPlan(mealPlanData) {
    // In a real app, this would save to a database
    // For now, we'll save to localStorage
    const savedPlans = JSON.parse(localStorage.getItem('savedMealPlans') || '[]');
    const newPlan = {
        id: Date.now(),
        date: new Date().toISOString(),
        ...mealPlanData
    };
    savedPlans.push(newPlan);
    localStorage.setItem('savedMealPlans', JSON.stringify(savedPlans));
    
    showFlashMessage('Meal plan saved successfully!', 'success');
}

// Load saved meal plans
function loadSavedPlans() {
    const savedPlans = JSON.parse(localStorage.getItem('savedMealPlans') || '[]');
    const plansContainer = document.querySelector('#savedPlansContainer');
    
    if (plansContainer && savedPlans.length > 0) {
        plansContainer.innerHTML = '';
        savedPlans.reverse().forEach(plan => {
            const planElement = createPlanElement(plan);
            plansContainer.appendChild(planElement);
        });
    } else if (plansContainer) {
        plansContainer.innerHTML = '<p class="no-plans">No saved meal plans yet. Create your first plan!</p>';
    }
}

// Create plan element for display
function createPlanElement(plan) {
    const planElement = document.createElement('div');
    planElement.className = 'saved-plan';
    planElement.innerHTML = `
        <div class="plan-header">
            <h3>Meal Plan - ${new Date(plan.date).toLocaleDateString()}</h3>
            <button class="btn btn-small btn-secondary" onclick="deletePlan(${plan.id})">Delete</button>
        </div>
        <div class="plan-summary">
            <span>Target: ${plan.target_calories} calories</span>
            <span>Total: ${plan.total_calories} calories</span>
        </div>
    `;
    return planElement;
}

// Delete saved plan
function deletePlan(planId) {
    const savedPlans = JSON.parse(localStorage.getItem('savedMealPlans') || '[]');
    const updatedPlans = savedPlans.filter(plan => plan.id !== planId);
    localStorage.setItem('savedMealPlans', JSON.stringify(updatedPlans));
    loadSavedPlans();
    showFlashMessage('Meal plan deleted successfully!', 'success');
}

// Initialize saved plans on page load
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('saved-plans')) {
        loadSavedPlans();
    }
}); 