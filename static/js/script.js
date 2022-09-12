/* Variables */
const menuBtn = document.getElementsByClassName('menu-btn')[0]
const linksCopy = document.getElementsByClassName('links')[0].cloneNode(true)
const nav = document.getElementsByClassName('main-nav')[0]
const searchCopy = document.getElementsByClassName('search-form')[0].cloneNode(true)
const account = document.getElementById('account')
const accountChildren = Array.from(account.children)
const accountLinks = document.getElementById('account-links')
const header = document.getElementById('main-header')

/* Declaring the dropdown Account divs from the cloned node */
const dropdownAccount = linksCopy.childNodes[7]
const dropdownAccountLinks = dropdownAccount.childNodes[5]

/* Append the cloned variables to the document and hide them initially */
nav.appendChild(linksCopy)
linksCopy.appendChild(searchCopy)
linksCopy.classList.add('hide')

/* Hide the Account Links initially  on both navs*/
accountLinks.classList.add('hide')
console.log(dropdownAccountLinks)
dropdownAccountLinks.classList.add('hide')


/* Set the status of the burger */
let burgerStatus = 'open'

/* Set the status of the Account nav  */
let accountStatus = 'closed'
let dropdownAccountStatus = 'closed'

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
        linksCopy.style.height = '100vh'
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
/* Function to handle the click on the account nav item */
const handleAccountClick = () => {
    if (accountStatus === 'closed') {
        accountLinks.classList.remove('hide')
        accountStatus = 'open'
    }
    else if (accountStatus === 'open'){
        accountStatus = 'closed'
        accountLinks.classList.add('links-close')
        /* Set a timeout to allow the animation to run before hiding the content */
        setTimeout(() => {
            accountLinks.classList.remove('links-close')
            accountLinks.classList.add('hide')
    }, 500)
    }
}

/* Function to handle the account click on smaller screens */
const handleDropdownAccountClick = () => {
    if (dropdownAccountStatus === 'closed') {
        dropdownAccountLinks.classList.remove('hide')
        dropdownAccountStatus = 'open'
    }
    else if (dropdownAccountStatus === 'open'){
        dropdownAccountStatus = 'closed'
        dropdownAccountLinks.classList.add('links-close')
        /* Set a timeout to allow the animation to run before hiding the content */
        setTimeout(() => {
            dropdownAccountLinks.classList.remove('links-close')
            dropdownAccountLinks.classList.add('hide')
    }, 500)
    }
}

/* Handle the clicking of the burger icon to show the nav and hide it again */
menuBtn.addEventListener('click', handleBurgerClick)

/* Set the Listener on the account element */
account.addEventListener('click', handleAccountClick)

/* Hide dropdown nav when mouse leaves */
accountLinks.addEventListener('mouseleave', handleAccountClick)

/* Set the event listener for the dropdown nav on smaller screens */
dropdownAccount.addEventListener('click', handleDropdownAccountClick)

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

/* Show the Nav on page laod */
document.addEventListener('DOMContentLoaded', function() {
    header.classList.add('slide-down')
})

document.removeEventListener('DOMContentLoaded', function() {
    header.classList.add('slide-down')
})