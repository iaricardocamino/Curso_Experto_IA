// Inicializar Iconos
lucide.createIcons();

let isEditing = false;

function toggleEditMode() {
    isEditing = !isEditing;
    document.body.classList.toggle('editing', isEditing);
    
    const btn = document.getElementById('edit-mode-btn');
    btn.classList.toggle('active', isEditing);
    
    const editableElements = document.querySelectorAll('[contenteditable]');
    editableElements.forEach(el => {
        el.setAttribute('contenteditable', isEditing ? 'true' : 'false');
    });

    btn.querySelector('i').setAttribute('data-lucide', isEditing ? 'check' : 'edit-3');
    lucide.createIcons();
}

function toggleTheme() {
    document.body.classList.toggle('dark');
    const icon = document.getElementById('theme-icon');
    const isDark = document.body.classList.contains('dark');
    icon.setAttribute('data-lucide', isDark ? 'sun' : 'moon');
    lucide.createIcons();
}

function changeImage() {
    if (!isEditing) return;
    const newUrl = prompt("Introduce la URL de la nueva imagen:");
    if (newUrl) {
        document.getElementById('profile-img').src = newUrl;
    }
}

function editSkill(bar) {
    if (!isEditing) return;
    const newVal = prompt("Introduce el porcentaje (0-100):", bar.parentElement.querySelector('.skill-val').innerText.replace('%',''));
    if (newVal !== null && !isNaN(newVal)) {
        const percent = Math.min(Math.max(parseInt(newVal), 0), 100);
        bar.querySelector('.progress-fill').style.width = percent + '%';
        bar.parentElement.querySelector('.skill-val').innerText = percent + '%';
    }
}

function prepareAndPrint() {
    if (isEditing) toggleEditMode();
    setTimeout(() => {
        window.print();
    }, 150);
}

document.addEventListener('keydown', (e) => {
    if (['H1', 'H3'].includes(e.target.tagName) || e.target.classList.contains('pill')) {
        if (e.key === 'Enter') e.preventDefault();
    }
});