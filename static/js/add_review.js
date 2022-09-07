/* Variables */
const addArtistBtn = document.getElementById('add-artist-btn');
const artistForm = document.getElementById('add-artist')
const searchInfoForm = document.getElementById('search-info-form')
let searchTitle = document.getElementsByClassName('search-title')[0]
let searchResults = document.getElementById('search-results')
const searchResultsContainer = document.getElementById('search-results-container')
const spinnerDiv = document.getElementById('spinner-div')
var pageId = 0

/* Adding custom first values to foreign key select form */
let yearOfRelease = document.getElementById('id_year_of_release')
yearOfRelease.children[0].innerText = 'Choose Year of Release'

let recordCompany = document.getElementById('id_record_company')
recordCompany.children[0].innerText = 'Choose Record Company'

let artist= document.getElementById('id_artist')
artist.children[0].innerText = 'Choose Artist'

let genre = document.getElementById('id_genre')
genre.children[0].innerText = 'Choose Genre'

let album = document.getElementById('id_album')
album.children[0].innerText = 'Choose Album to Review'

/* Adding event listeners to the buttons */

showBtns = Array.from(document.getElementsByClassName('add-btn'))
formDivs = Array.from(document.getElementsByClassName('form-div'))

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
    formDivs.forEach((div) => {
        if (btn.dataset.type === div.dataset.type) {
            setTimeout(() => {
                div.classList.remove('hide')
                div.classList.add('fade-in-form')
                setTimeout(() => {
                    div.classList.remove('fade-in-form')
                }, 500)
            }, 500);
        }
        else {
            div.classList.add('fade-out-form')
            setTimeout(() => {
                div.classList.add('hide')
                div.classList.remove('fade-out-form')
            }, 500)
        }
    })
}

/* From Wikipedia Official docs */

// Getting the text from the form and inputting it into the API call

searchInfoForm.addEventListener('submit', function(event) {
    event.preventDefault()
    let searchTerm = document.getElementById('search-data').value

    // Hide Previousthe results box if visible
    searchResultsContainer.classList.add('hide')
    // Show the loading spinner
    spinnerDiv.classList.remove('hide')

    // Setting the params for the first API call
    let parameters = {
        action: "query",
        list: "search",
        srsearch: searchTerm,
        format: "json"
};
    returnData(parameters)
})


const returnData = (params) => {

    var url = "https://en.wikipedia.org/w/api.php"; 

    url = url + "?origin=*";
    Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

    fetch(url)
        .then(function(response){return response.json();})
        .then(function(response) {
            if (response.query && params.list === 'search'){
                searchTitle.innerText = response.query.search[0].title
                pageId = response.query.search[0].pageid
                // Assign new prameters from the search to try and get the content of a searched page
                newParameters = {
                    format: 'json',
                    action: 'query',
                    prop: 'extracts',
                    redirects: 1,
                    pageids: response.query.search[0].pageid
                }
                returnData(newParameters)
            }
            // If the result was found render the content to the screen
            else if (response.query.pages[pageId]) {
                searchResults.innerHTML = response.query.pages[pageId].extract
                spinnerDiv.classList.add('hide')
                searchResultsContainer.classList.remove('hide')
            }
            // If result was not found render a message
            else {
                spinnerDiv.classList.add('hide')
                searchResultsContainer.classList.remove('hide')
                searchResults.innerText = 'Please search with a different search word as this has not resulted in the correct data being retrieved'
            }
        })
        // If the initial search has an error ask the user to search again
        .catch(function(error){
            console.log(error);
            spinnerDiv.classList.add('hide')
            searchResultsContainer.classList.remove('hide')
            searchResults.innerText = 'Please search with a different search word as this has not resulted in the correct data being retrieved'
        });
    }