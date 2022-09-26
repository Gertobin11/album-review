/* Variables */
const searchInfoForm = document.getElementById('search-info-form')
let searchTitle = document.getElementsByClassName('search-title')[0]
let searchResults = document.getElementById('search-results')
const searchResultsContainer = document.getElementById('search-results-container')
const spinnerDiv = document.getElementById('spinner-div')
var pageId = 0


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