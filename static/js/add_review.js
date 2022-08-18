/* Variables */
const addArtistBtn = document.getElementById('add-artist-btn');
const artistForm = document.getElementById('add-artist')

/* Adding custom first values to foreign key select form */
let yearOfRelease = document.getElementById('id_year_of_release')
yearOfRelease.children[0].innerText = 'Choose Year of Release'

let recordCompany = document.getElementById('id_record_company')
recordCompany.children[0].innerText = 'Choose Record Company'

let artist= document.getElementById('id_artist')
artist.children[0].innerText = 'Choose Artist'

let genre = document.getElementById('id_genre')
genre.children[0].innerText = 'Choose Genre'

/* Adding event listeners to the buttons */

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
        let albumCover = document.getElementById('file-upload-button')
        console.log(albumCover)
    }
}
