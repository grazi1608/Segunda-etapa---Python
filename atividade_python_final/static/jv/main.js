document.addEventListener('DOMContentLoaded', () => {
    const themeBtn = document.getElementById('toggle-theme');
    const themeIcon = document.getElementById('theme-icon');
    const htmlElement = document.documentElement; // Seleciona a tag <html>

    // 1. Carrega o tema salvo no localStorage (ou 'light' por padrão)
    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-bs-theme', savedTheme);
    atualizarIcone(savedTheme);

    // 2. Evento de clique no botão
    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            const currentTheme = htmlElement.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            // Aplica o novo tema no atributo da tag <html>
            htmlElement.setAttribute('data-bs-theme', newTheme);
            
            // Salva a preferência no navegador
            localStorage.setItem('theme', newTheme);
            
            // Atualiza o ícone do botão
            atualizarIcone(newTheme);
        });
    }

    function atualizarIcone(theme) {
        if (themeIcon) {
            themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
        }
    }
});