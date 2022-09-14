document.addEventListener("DOMContentLoaded", function () {
  let reviewCards = Array.from(
    document.getElementsByClassName("latest-reviews-card")
  );

  const mainCards = Array.from(document.getElementById('main-content').children)

  const accountLinks = document.getElementById('account-links')

  var openMenu = false

  let profileCards =  Array.from(
    document.getElementsByClassName("top-profiles-card")
  );

  let profileSection = document.getElementById('top-profiles')
  let reviewsSection = document.getElementById('latest-reviews')
  let accountSpan = document.getElementById('account-span')
  let menuBtnBrgr = document.getElementsByClassName('menu-btn__burger')[0]
  let messages = Array.from(document.getElementsByClassName('message-card'))
  console.log(messages)

  /*
  * Move the profile and review cards back 
  * So the dropdown nav can appear
  * Also put them back up after a the cursor leaves
  * the dropdown
  */

  accountSpan.addEventListener('click', function() {
    !openMenu ?  (
      moveCardsBack([profileSection, reviewsSection, ...mainCards]),
      openMenu = true) : (
        moveUpCards([profileSection, reviewsSection, ...mainCards]),
      openMenu = false
      )
  })

  /* 
  * Hide the profile card behind the hamburd=ger menu 
  * on smaller screens
  */

  menuBtnBrgr.addEventListener('click', function() {
    !openMenu ?  (
      moveCardsBack([profileSection, reviewsSection, ...mainCards]),
      openMenu = true) 
    : (
        moveUpCards([profileSection, reviewsSection, ...mainCards]),
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

   /*
  * Function to animate the main content cards
  * on Mobile and smaller screen devices
  */

  let n = 200
  mainCards.forEach((card) => {
    setTimeout(() => {
      card.classList.add('slide-in-main-cards')
    }, n + 100)
    n += 150,
    console.log(n)
  })

  /*
  * Move the cards behind the messages if there are any 
  * to display to the user
  */
  if (messages) {
    moveCardsBack([profileSection, reviewsSection, ...mainCards])
    openMenu = true
    setTimeout(() => {
      moveUpCards([profileSection, reviewsSection, ...mainCards])
      openMenu = false
    }, 3000)
  }
   
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
