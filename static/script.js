const btn = document.querySelector('.drop-btn')
const menu = document.querySelector('.dropdown-menu')

btn.addEventListener('click', function() {
    if (menu.style.display === 'none') {
        menu.style.display = 'block'
    } else {
        menu.style.display = 'none'
    }
})