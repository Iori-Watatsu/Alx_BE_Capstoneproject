// Authentication JavaScript for Bloom Beauty

class AuthManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupFormValidation();
        this.setupPasswordVisibility();
        this.setupAutoLogout();
        this.setupSessionManagement();
        this.setupAuthEvents();
    }

    setupFormValidation() {
        // Real-time form validation
        document.addEventListener('input', (e) => {
            if (e.target.matches('.auth-form input')) {
                this.validateField(e.target);
            }
        });

        // Form submission validation
        document.addEventListener('submit', (e) => {
            const form = e.target;
            if (form.classList.contains('auth-form')) {
                if (!this.validateForm(form)) {
                    e.preventDefault();
                    this.showFormErrors(form);
                }
            }
        });
    }

    validateField(field) {
        const form = field.closest('form');
        const errorDiv = field.parentElement.querySelector('.input-error') ||
                        document.getElementById(field.id + 'Error');

        if (!errorDiv) return true;

        let isValid = true;
        let message = '';

        switch(field.type) {
            case 'email':
                isValid = this.validateEmail(field.value);
                message = isValid ? '' : 'Please enter a valid email address';
                break;

            case 'password':
                if (field.id.includes('password1') || field.id.includes('new_password1')) {
                    const strength = securityManager.checkPasswordStrength(field.value);
                    isValid = strength.score >= 3;
                    message = isValid ? '' : 'Password is too weak';
                }
                break;

            case 'text':
                if (field.name === 'username') {
                    isValid = this.validateUsername(field.value);
                    message = isValid ? '' : 'Username must be 3-30 characters (letters, numbers, underscores)';
                }
                break;
        }

        if (field.required && !field.value.trim()) {
            isValid = false;
            message = 'This field is required';
        }

        errorDiv.textContent = message;
        field.classList.toggle('invalid', !isValid);
        field.classList.toggle('valid', isValid && field.value.trim() !== '');

        return isValid;
    }

    validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    validateUsername(username) {
        const re = /^[a-zA-Z0-9_]{3,30}$/;
        return re.test(username);
    }

    validateForm(form) {
        let isValid = true;
        const inputs = form.querySelectorAll('input[required], textarea[required]');

        inputs.forEach(input => {
            if (!this.validateField(input)) {
                isValid = false;
            }
        });

        // Special validation for password confirmation
        const password1 = form.querySelector('input[name*="password1"], input[name*="new_password1"]');
        const password2 = form.querySelector('input[name*="password2"], input[name*="new_password2"]');

        if (password1 && password2 && password1.value !== password2.value) {
            const errorDiv = password2.parentElement.querySelector('.input-error') ||
                           document.getElementById(password2.id + 'Error');
            if (errorDiv) {
                errorDiv.textContent = 'Passwords do not match';
                password2.classList.add('invalid');
            }
            isValid = false;
        }

        return isValid;
    }

    showFormErrors(form) {
        const firstError = form.querySelector('.invalid');
        if (firstError) {
            firstError.focus();
            this.showToast('Please fix the errors in the form', 'error');
        }
    }

    setupPasswordVisibility() {
        document.addEventListener('click', (e) => {
            if (e.target.closest('.password-toggle')) {
                const toggle = e.target.closest('.password-toggle');
                const input = toggle.closest('.password-wrapper').querySelector('input');
                const icon = toggle.querySelector('i');

                if (input.type === 'password') {
                    input.type = 'text';
                    icon.classList.remove('fa-eye');
                    icon.classList.add('fa-eye-slash');
                } else {
                    input.type = 'password';
                    icon.classList.remove('fa-eye-slash');
                    icon.classList.add('fa-eye');
                }
            }
        });
    }

    setupAutoLogout() {
        // Auto-logout after 30 minutes of inactivity
        let timeout;
        const logoutTime = 30 * 60 * 1000; // 30 minutes

        const resetTimer = () => {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                if (this.isUserLoggedIn()) {
                    this.showLogoutWarning();
                }
            }, logoutTime);
        };

        // Reset timer on user activity
        ['mousedown', 'keydown', 'touchstart'].forEach(event => {
            document.addEventListener(event, resetTimer);
        });

        resetTimer();
    }

    isUserLoggedIn() {
        // Check if user is authenticated
        return document.body.classList.contains('user-authenticated') ||
               document.querySelector('.auth-required') === null;
    }

    showLogoutWarning() {
        if (document.querySelector('.logout-warning')) return;

        const warning = document.createElement('div');
        warning.className = 'logout-warning';
        warning.innerHTML = `
            <i class="fas fa-clock"></i>
            <span>You will be logged out due to inactivity in 2 minutes.</span>
            <div>
                <button onclick="authManager.stayLoggedIn()">Stay Logged In</button>
                <button onclick="authManager.logoutNow()">Logout Now</button>
            </div>
        `;

        document.body.appendChild(warning);
        setTimeout(() => warning.classList.add('show'), 100);

        // Auto-logout after 2 minutes
        this.logoutTimeout = setTimeout(() => {
            this.performLogout();
        }, 2 * 60 * 1000);
    }

    stayLoggedIn() {
        clearTimeout(this.logoutTimeout);
        const warning = document.querySelector('.logout-warning');
        if (warning) {
            warning.remove();
        }
        this.setupAutoLogout(); // Reset timer
    }

    logoutNow() {
        clearTimeout(this.logoutTimeout);
        this.performLogout();
    }

    performLogout() {
        // Submit logout form
        const logoutForm = document.querySelector('form[action*="logout"]');
        if (logoutForm) {
            logoutForm.submit();
        } else {
            window.location.href = '/logout/';
        }
    }

    setupSessionManagement() {
        // Monitor multiple tabs
        window.addEventListener('storage', (e) => {
            if (e.key === 'session_ended' && e.newValue) {
                this.showToast('Session ended in another tab', 'warning');
                setTimeout(() => {
                    window.location.reload();
                }, 2000);
            }
        });

        // Mark session as active
        setInterval(() => {
            if (this.isUserLoggedIn()) {
                localStorage.setItem('session_active', Date.now());
            }
        }, 30000);
    }

    setupAuthEvents() {
        // Handle login success
        if (window.location.search.includes('login=success')) {
            this.showToast('Successfully logged in!', 'success');
            this.trackLoginEvent();
        }

        // Handle logout
        if (window.location.pathname.includes('logout')) {
            this.clearAuthData();
        }
    }

    trackLoginEvent() {
        // Track login for security monitoring
        const eventData = {
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            language: navigator.language
        };

        // Send to analytics/security endpoint
        console.log('Login event:', eventData);
    }

    clearAuthData() {
        // Clear sensitive data from storage
        localStorage.removeItem('session_active');
        sessionStorage.clear();

        // Clear any auth tokens from memory
        delete window.authToken;
    }

    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `auth-toast auth-toast-${type}`;
        toast.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
            <span>${message}</span>
            <button onclick="this.parentElement.remove()">&times;</button>
        `;

        document.body.appendChild(toast);
        setTimeout(() => toast.classList.add('show'), 100);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 5000);
    }

    // Password reset functionality
    requestPasswordReset(email) {
        if (!this.validateEmail(email)) {
            this.showToast('Please enter a valid email address', 'error');
            return;
        }

        // Show loading
        this.showToast('Sending reset instructions...', 'info');

        // In production, this would be an API call
        fetch('/api/password-reset/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': securityManager.getCSRFToken()
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                this.showToast('Reset instructions sent to your email', 'success');
            } else {
                this.showToast(data.message || 'Reset request failed', 'error');
            }
        })
        .catch(error => {
            console.error('Password reset error:', error);
            this.showToast('An error occurred. Please try again.', 'error');
        });
    }
}

// Initialize auth manager
const authManager = new AuthManager();

// Auth CSS
const authStyles = `
.auth-toast {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #333;
    color: white;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    z-index: 4000;
    display: flex;
    align-items: center;
    gap: 12px;
    max-width: 400px;
    transform: translateY(100%);
    opacity: 0;
    transition: all 0.3s ease;
}

.auth-toast.show {
    transform: translateY(0);
    opacity: 1;
}

.auth-toast i {
    font-size: 20px;
}

.auth-toast.auth-toast-success i { color: #34C759; }
.auth-toast.auth-toast-error i { color: #FF3B30; }
.auth-toast.auth-toast-warning i { color: #FF9500; }
.auth-toast.auth-toast-info i { color: #007AFF; }

.auth-toast span {
    flex: 1;
    font-size: 14px;
}

.auth-toast button {
    background: none;
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    padding: 0;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.logout-warning {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%) translateY(-100%);
    background: #FF9500;
    color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 30px rgba(0,0,0,0.3);
    z-index: 4000;
    max-width: 500px;
    width: 90%;
    transition: transform 0.3s ease;
}

.logout-warning.show {
    transform: translateX(-50%) translateY(0);
}

.logout-warning i {
    font-size: 24px;
    margin-bottom: 12px;
    display: block;
    text-align: center;
}

.logout-warning span {
    display: block;
    text-align: center;
    margin-bottom: 16px;
    font-size: 15px;
}

.logout-warning div {
    display: flex;
    gap: 12px;
}

.logout-warning button {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.logout-warning button:first-child {
    background: white;
    color: #FF9500;
}

.logout-warning button:last-child {
    background: rgba(255,255,255,0.2);
    color: white;
}

.logout-warning button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

/* Form validation styles */
input.invalid {
    border-color: #FF3B30 !important;
    background: #FFF5F5 !important;
}

input.valid {
    border-color: #34C759 !important;
    background: #F5FFF7 !important;
}

@media (max-width: 768px) {
    .auth-toast {
        left: 20px;
        right: 20px;
        max-width: none;
    }

    .logout-warning div {
        flex-direction: column;
    }
}
`;

// Add auth styles to document
const authStyleSheet = document.createElement('style');
authStyleSheet.textContent = authStyles;
document.head.appendChild(authStyleSheet);

// Export for use in other modules
window.AuthManager = AuthManager;
window.authManager = authManager;

// Utility functions for global use
window.togglePassword = function(inputId) {
    const input = document.getElementById(inputId);
    if (!input) return;

    const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
    input.setAttribute('type', type);
};

window.showIOSAlert = function(title, message) {
    // iOS-style alert implementation
    const modal = document.createElement('div');
    modal.className = 'ios-alert-modal';
    modal.innerHTML = `
        <div class="ios-alert-content">
            <h3>${title}</h3>
            <p>${message}</p>
            <button class="ios-btn-primary" onclick="this.closest('.ios-alert-modal').remove()">OK</button>
        </div>
    `;

    document.body.appendChild(modal);
    setTimeout(() => modal.classList.add('show'), 100);
};

window.openModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'flex';
        setTimeout(() => modal.classList.add('active'), 100);
    }
};

window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    }
};