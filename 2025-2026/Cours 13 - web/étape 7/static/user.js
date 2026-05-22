const form = document.getElementById('user-form');
const errorBox = document.getElementById('form-error');

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidPassword(password) {
    const hasMinLength = password.length >= 8;
    const hasUpper = /[A-Z]/.test(password);
    const hasLower = /[a-z]/.test(password);
    const hasDigit = /\d/.test(password);
    const hasSpecial = /[^A-Za-z0-9]/.test(password);
    return hasMinLength && hasUpper && hasLower && hasDigit && hasSpecial;
}

if (form && errorBox) {
    form.addEventListener('submit', (event) => {
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;

        if (!isValidEmail(email)) {
            event.preventDefault();
            errorBox.textContent = "Erreur : l'email n'est pas valide.";
            return;
        }

        if (!isValidPassword(password)) {
            event.preventDefault();
            errorBox.textContent = "Erreur : le mot de passe doit contenir au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial.";
            return;
        }

        errorBox.textContent = '';
    });
}

