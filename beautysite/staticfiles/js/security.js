// Security Utilities for Bloom Beauty

class SecurityManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupSecurityHeaders();
        this.setupCSRFProtection();
        this.setupInputSanitization();
        this.setupClickjackingProtection();
        this.setupTimingAttackProtection();
        this.setupSessionSecurity();
    }

    setupSecurityHeaders() {
        // Remove sensitive headers if accidentally set by server
        if (window.location.protocol !== 'https:') {
            console.warn('Site not using HTTPS. Consider enabling SSL.');
        }
    }

    setupCSRFProtection() {
        // Ensure CSRF token is present in all forms
        document.addEventListener('submit', (e) => {
            const form = e.target;
            if (form.method.toUpperCase() === 'POST') {
                const token = this.getCSRFToken();
                if (!token) {
                    console.warn('CSRF token missing');
                    e.preventDefault();
                    this.showSecurityAlert('Security check failed. Please refresh the page.');
                    return;
                }
            }
        });
    }

    getCSRFToken() {
        return document.querySelector('meta[name="csrf-token"]')?.content ||
               document.querySelector('[name="csrfmiddlewaretoken"]')?.value;
    }

    setupInputSanitization() {
        // Sanitize user inputs
        const sanitizeInput = (input) => {
            if (!input) return '';

            // Remove potentially dangerous characters
            return input
                .replace(/[<>]/g, '') // Remove < and >
                .replace(/javascript:/gi, '') // Remove javascript: protocol
                .replace(/on\w+=/gi, '') // Remove event handlers
                .trim();
        };

        // Apply to all text inputs
        document.addEventListener('input', (e) => {
            if (e.target.matches('input[type="text"], input[type="email"], textarea')) {
                e.target.value = sanitizeInput(e.target.value);
            }
        });
    }

    setupClickjackingProtection() {
        // Prevent iframe embedding
        if (window.self !== window.top) {
            window.top.location = window.self.location;
        }

        // Add X-Frame-Options via meta tag (backup)
        if (!document.querySelector('meta[http-equiv="X-Frame-Options"]')) {
            const meta = document.createElement('meta');
            meta.httpEquiv = 'X-Frame-Options';
            meta.content = 'DENY';
            document.head.appendChild(meta);
        }
    }

    setupTimingAttackProtection() {
        // Add random delay to form submissions
        document.addEventListener('submit', (e) => {
            const form = e.target;
            if (form.classList.contains('auth-form')) {
                const delay = 100 + Math.random() * 200; // 100-300ms
                e.preventDefault();

                setTimeout(() => {
                    form.submit();
                }, delay);
            }
        });
    }

    setupSessionSecurity() {
        // Monitor session activity
        let lastActivity = Date.now();

        document.addEventListener('mousemove', () => lastActivity = Date.now());
        document.addEventListener('keypress', () => lastActivity = Date.now());

        // Check for inactivity every minute
        setInterval(() => {
            const inactiveTime = Date.now() - lastActivity;
            const sessionTimeout = 30 * 60 * 1000; // 30 minutes

            if (inactiveTime > sessionTimeout) {
                this.showSessionWarning();
            }
        }, 60000);
    }

    showSessionWarning() {
        if (document.querySelector('.session-warning')) return;

        const warning = document.createElement('div');
        warning.className = 'session-warning';
        warning.innerHTML = `
            <i class="fas fa-clock"></i>
            <span>Your session will expire soon due to inactivity.</span>
            <button onclick="securityManager.extendSession()">Extend Session</button>
        `;

        document.body.appendChild(warning);
        setTimeout(() => warning.classList.add('show'), 100);

        // Auto-remove after 10 seconds
        setTimeout(() => {
            warning.classList.remove('show');
            setTimeout(() => warning.remove(), 300);
        }, 10000);
    }

    extendSession() {
        // Send keep-alive request
        fetch('/api/session/keepalive/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': this.getCSRFToken()
            }
        }).then(() => {
            const warning = document.querySelector('.session-warning');
            if (warning) {
                warning.innerHTML = `
                    <i class="fas fa-check"></i>
                    <span>Session extended!</span>
                `;
                setTimeout(() => warning.remove(), 2000);
            }
        });
    }

    showSecurityAlert(message) {
        const alert = document.createElement('div');
        alert.className = 'security-alert';
        alert.innerHTML = `
            <i class="fas fa-shield-alt"></i>
            <span>${message}</span>
            <button onclick="this.parentElement.remove()">&times;</button>
        `;

        document.body.appendChild(alert);
        setTimeout(() => alert.classList.add('show'), 100);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            alert.classList.remove('show');
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    }

    // Password strength checker
    checkPasswordStrength(password) {
        let score = 0;

        // Length check
        if (password.length >= 12) score++;
        if (password.length >= 16) score++;

        // Character variety
        if (/[a-z]/.test(password)) score++;
        if (/[A-Z]/.test(password)) score++;
        if (/[0-9]/.test(password)) score++;
        if (/[^A-Za-z0-9]/.test(password)) score++;

        // Common password check
        const commonPasswords = [
            'password', '123456', 'qwerty', 'letmein', 'welcome',
            'monkey', 'dragon', 'baseball', 'football', 'mustang'
        ];

        if (commonPasswords.includes(password.toLowerCase())) {
            score = 0;
        }

        // Dictionary check (simplified)
        if (password.length <= 6 && /^[a-z]+$/i.test(password)) {
            score = Math.max(score - 2, 0);
        }

        return {
            score: Math.min(score, 5),
            level: ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong', 'Excellent'][Math.min(score, 5)]
        };
    }

    // Generate secure token
    generateSecureToken(length = 32) {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        const crypto = window.crypto || window.msCrypto;

        if (crypto && crypto.getRandomValues) {
            const array = new Uint8Array(length);
            crypto.getRandomValues(array);
            return Array.from(array, byte => chars[byte % chars.length]).join('');
        }

        // Fallback for older browsers
        let token = '';
        for (let i = 0; i < length; i++) {
            token += chars[Math.floor(Math.random() * chars.length)];
        }
        return token;
    }

    // Detect and prevent brute force
    setupBruteForceProtection() {
        let attemptCount = 0;
        const maxAttempts = 5;
        const lockoutTime = 15 * 60 * 1000; // 15 minutes

        document.addEventListener('submit', (e) => {
            const form = e.target;
            if (form.id === 'loginForm') {
                attemptCount++;

                if (attemptCount >= maxAttempts) {
                    e.preventDefault();
                    this.lockAccount();
                }

                // Store attempts in sessionStorage
                sessionStorage.setItem('login_attempts', attemptCount);
            }
        });

        // Check for existing lockout
        const lockoutUntil = localStorage.getItem('account_lockout');
        if (lockoutUntil && Date.now() < parseInt(lockoutUntil)) {
            this.showLockoutMessage(lockoutUntil);
        }
    }

    lockAccount() {
        const lockoutUntil = Date.now() + (15 * 60 * 1000);
        localStorage.setItem('account_lockout', lockoutUntil);

        this.showLockoutMessage(lockoutUntil);
    }

    showLockoutMessage(lockoutUntil) {
        const minutes = Math.ceil((lockoutUntil - Date.now()) / 60000);

        const message = document.createElement('div');
        message.className = 'lockout-message';
        message.innerHTML = `
            <i class="fas fa-lock"></i>
            <div>
                <h4>Account Temporarily Locked</h4>
                <p>Too many failed attempts. Try again in ${minutes} minutes.</p>
                <p>If this was you, <a href="/password-reset/">reset your password</a>.</p>
            </div>
        `;

        document.body.appendChild(message);
        setTimeout(() => message.classList.add('show'), 100);
    }

    // XSS Protection
    sanitizeHTML(html) {
        const temp = document.createElement('div');
        temp.textContent = html;
        return temp.innerHTML;
    }

    // Secure storage
    secureStorage = {
        set: function(key, value) {
            try {
                const encrypted = btoa(encodeURIComponent(JSON.stringify(value)));
                localStorage.setItem('secure_' + key, encrypted);
            } catch (e) {
                console.warn('Local storage not available');
            }
        },

        get: function(key) {
            try {
                const encrypted = localStorage.getItem('secure_' + key);
                if (!encrypted) return null;
                return JSON.parse(decodeURIComponent(atob(encrypted)));
            } catch (e) {
                return null;
            }
        },

        remove: function(key) {
            localStorage.removeItem('secure_' + key);
        }
    };
}

// Initialize security manager
const securityManager = new SecurityManager();

// Security CSS
const securityStyles = `
.security-alert,
.session-warning,
.lockout-message {
    position: fixed;
    top: 20px;
    right: 20px;
    background: #FF3B30;
    color: white;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    z-index: 4000;
    display: flex;
    align-items: center;
    gap: 12px;
    max-width: 400px;
    transform: translateX(120%);
    transition: transform 0.3s ease;
}

.security-alert.show,
.session-warning.show,
.lockout-message.show {
    transform: translateX(0);
}

.security-alert i,
.session-warning i,
.lockout-message i {
    font-size: 20px;
}

.security-alert span,
.session-warning span,
.lockout-message span {
    flex: 1;
    font-size: 14px;
}

.security-alert button,
.session-warning button,
.lockout-message button {
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

.session-warning {
    background: #FF9500;
}

.lockout-message {
    background: #FF3B30;
    text-align: left;
}

.lockout-message div {
    flex: 1;
}

.lockout-message h4 {
    margin: 0 0 4px 0;
    font-size: 15px;
    font-weight: 600;
}

.lockout-message p {
    margin: 0 0 8px 0;
    font-size: 13px;
    opacity: 0.9;
}

.lockout-message a {
    color: white;
    text-decoration: underline;
}

@media (max-width: 768px) {
    .security-alert,
    .session-warning,
    .lockout-message {
        left: 20px;
        right: 20px;
        max-width: none;
    }
}
`;

// Add security styles to document
const styleSheet = document.createElement('style');
styleSheet.textContent = securityStyles;
document.head.appendChild(styleSheet);

// Export for use in other modules
window.SecurityManager = SecurityManager;
window.securityManager = securityManager;