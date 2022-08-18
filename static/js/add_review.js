/* Variables */
const addArtistBtn = document.getElementById('add-artist-btn');
const artistForm = document.getElementById('add-artist')
let showArtistForm = false

addArtistBtn.addEventListener('click', () => {
    if (showArtistForm === false) {
        artistForm.classList.remove('hide');
        addArtistBtn.innerText = 'Hide Form';
        showArtistForm = true;
    }
    else if (showArtistForm) {
        artistForm.classList.add('hide')
        addArtistBtn.innerText = 'Add an Artist'
        showArtistForm = false
    }
})
