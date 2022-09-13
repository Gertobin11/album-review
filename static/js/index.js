document.addEventListener("DOMContentLoaded", function () {
  let reviewCards = Array.from(
    document.getElementsByClassName("latest-reviews-card")
  );

  const accountLinks = document.getElementById('account-links')

  var openMenu = false

  let profileCards =  Array.from(
    document.getElementsByClassName("top-profiles-card")
  );

  let profileSection = document.getElementById('top-profiles')
  let reviewsSection = document.getElementById('latest-reviews')
  let accountSpan = document.getElementById('account-span')
  let menuBtnBrgr = document.getElementsByClassName('menu-btn__burger')[0]

  /*
  * Move the profile and review cards back 
  * So the dropdown nav can appear
  * Also put them back up after a the cursor leaves
  * the dropdown
  */

  accountSpan.addEventListener('click', function() {
    !openMenu ?  (
      moveCardsBack([profileSection, reviewsSection]),
      openMenu = true) : (
        moveUpCards([profileSection, reviewsSection]),
      openMenu = false
      )
  })

  /* 
  * Hide the profile card behind the hamburd=ger menu 
  * on smaller screens
  */

  menuBtnBrgr.addEventListener('click', function() {
    !openMenu ?  (
      moveCardsBack([profileSection, reviewsSection]),
      openMenu = true) 
    : (
        moveUpCards([profileSection, reviewsSection]),
        openMenu = false
      )
  })

  accountLinks.addEventListener('mouseleave', function() {
    moveUpCards([profileSection, reviewsSection])
    openMenu = false
  })

  /*
  * Call functions to apply transititions
  */
  applyTransition(profileCards)
  applyTransition(reviewCards)
  applyFadeIn(profileSection)
  applyFadeIn(reviewsSection)
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

function moveCardsBack(cards) {
  for (let card of cards) {
    card.style.zIndex = "-1"
  }
}

function moveUpCards(cards) {
  for (let card of cards) {
    card.style.zIndex = "1"
  }
}
