/* Variables */
const linkDiv = document.getElementsByClassName('links')[0]

const links = linkDiv.children

const linksCopy = linkDiv.cloneNode(true)

const nav = document.getElementsByClassName('main-nav')[0]

nav.appendChild(linksCopy)

const menuBtn = document.getElementsByClassName('menu-btn')[0]

/* Set the status of he burger */
let burgerStatus = 'open'

/* Handle the clicking of the burger icon to show the nav and hide it again */
menuBtn.addEventListener('click', () => {
    if (burgerStatus === 'open') {
        menuBtn.classList.add('open')
        linksCopy.classList.remove('links-close')
        linksCopy.classList.add('links-open')
        linksCopy.classList.add('show')
        burgerStatus = 'closed'
        nav.appendChild(linksCopy)
    }
    else if (burgerStatus === 'closed') {
        menuBtn.classList.remove('open')
        linksCopy.classList.add('links-close')
        burgerStatus = 'open'

        /* Set a timeout to allow the animation to run before hiding the content */
        setTimeout(() => {
            linksCopy.classList.remove('links-open')
            linksCopy.classList.remove('show')
    }, 500)
    }
})