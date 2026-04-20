const allMenus = document.querySelectorAll('.dropdown-menu')

function closeAll() {
    allMenus.forEach(function(menu) {
        menu.style.display = 'none'
    })
}

const dropdowns = document.querySelectorAll('.dropdown, .brand')
dropdowns.forEach(function(dropdown) {
    const btn = dropdown.querySelector('.drop-btn')
    const menu = dropdown.querySelector('.dropdown-menu')

    btn.addEventListener('click', function() {
        const isOpen = menu.style.display === 'block'
        closeAll()
        if (!isOpen) {
            menu.style.display = 'block'
        }
    })
})

const searchBtn = document.querySelector('.search-btn')
const searchInput = document.querySelector('.search-box input')

searchBtn.addEventListener('click', function() {
    const isOpen = searchInput.style.display === 'block'
    closeAll()
    if (!isOpen) {
        searchInput.style.display = 'block'
        searchInput.focus()
    }
})