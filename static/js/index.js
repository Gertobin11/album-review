document.addEventListener("DOMContentLoaded", function () {
  let reviewCards = Array.from(
    document.getElementsByClassName("latest-reviews-card")
  );

  let openMenu = 'closed'

  let profileCards =  Array.from(
    document.getElementsByClassName("top-profiles-card")
  );

  let profileSection = document.getElementById('top-profiles')
  let revewsSection = document.getElementById('latest-reviews')

  /*
* Move the profile and review cards back 
* So the dropdown nav can appear
* Also put them back up after a click elsewhere
*/

document.addEventListener('click', function(event) {
  if (event.target.innerText === ' Account' && openMenu === 'closed' ) {
    moveCardsBack(profileSection)
    moveCardsBack(revewsSection)
    openMenu = 'open'
  }

  else if (event.target.innerText === ' Account' && openMenu === 'open' ) {
    moveUpCards(profileSection)
    moveUpCards(revewsSection)
    openMenu = 'closed'
  }

  else if (event.target.className === 'menu-btn__burger' && openMenu === 'closed' ) {
    moveCardsBack(profileSection)
    moveCardsBack(revewsSection)
    openMenu = 'open'
  }

  else {
    moveUpCards(profileSection)
    moveUpCards(revewsSection)
    openMenu = 'closed'
  }
})

  /*
  * Call functions to apply transititions
  */
  applyTransition(profileCards)
  applyTransition(reviewCards)
  applyFadeIn(profileSection)
  applyFadeIn(revewsSection)
});

/*
* Apply the transition of the cards back into place
*/
function applyTransition(cards) {
  let time = 0;
  cards.forEach((card) => {
    setTimeout(() => {
      card.classList.add("slide-in-card");
    }, 200 + time);
    time += 200;
  });
}

function applyFadeIn(card) {
  card.classList.add('fade-in-sections')
}

function moveCardsBack(card) {
  card.style.zIndex = "-1"
}

function moveUpCards(card) {
  card.style.zIndex = "1"
}
