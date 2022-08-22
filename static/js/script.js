/* Variables */
const menuBtn = document.getElementsByClassName('menu-btn')[0]
const linksCopy = document.getElementsByClassName('links')[0].cloneNode(true)
const nav = document.getElementsByClassName('main-nav')[0]
const searchCopy = document.getElementsByClassName('search-form')[0].cloneNode(true)

/* Append the cloned variables to the document and hide them initially */
nav.appendChild(linksCopy)
linksCopy.appendChild(searchCopy)
linksCopy.classList.add('hide')

/* Set the status of the burger */
let burgerStatus = 'open'

const handleBurgerClick = () => {
    /* Function that opens and close the dropdown menu */
    if (burgerStatus === 'open') {
        menuBtn.classList.add('open')
        searchCopy.classList.add('search-form-drop')
        linksCopy.classList.remove('links-close')
        linksCopy.classList.add('links-open')
        linksCopy.classList.remove('hide')
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
            linksCopy.classList.add('hide')
            searchCopy.classList.remove('search-form-drop')
    }, 500)
    }
}

/* Handle the clicking of the burger icon to show the nav and hide it again */
menuBtn.addEventListener('click', handleBurgerClick)

/* Code to apply animation to messages and auto close the container */

let messages = Array.from(document.getElementsByClassName('message-card'))
let sleep = 0;

/* If multiple messages have them fade at different times */
messages.forEach((message) => {
    sleep += 300
    setTimeout(() => {
        message.classList.add('remove-message-animation');
        /* Setting an addtional timeout to remove the element afer the animation ends */
        setTimeout(() => {
            message.remove()
        }, 1000)
    }, 3500 + sleep)
})