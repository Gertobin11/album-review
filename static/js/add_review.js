/* Variables */
const addArtistBtn = document.getElementById('add-artist-btn');
const artistForm = document.getElementById('add-artist')

showBtns = Array.from(document.getElementsByClassName('add-btn'))

showBtns.forEach(btn => {
    btn.addEventListener('click', function(event) {
        hideShowForm(event.target)
    })
});

/*
* Function that will hide or show the matching
* form when the button is clicked
*/
const hideShowForm = (btn) => {
    if (btn.innerText === 'Hide') {
        btn.nextSibling.nextSibling.classList.add('hide')
        let btnText = btn.getAttribute('data-type')
        btn.innerText = `Add ${btnText}`
    }
    else {
        console.log(btn, 'else')
        btn.nextSibling.nextSibling.classList.remove('hide');
        btn.innerText = 'Hide';
    }
}
