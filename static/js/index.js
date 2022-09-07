document.addEventListener("DOMContentLoaded", function () {
  let reviewCards = Array.from(
    document.getElementsByClassName("latest-reviews-card")
  );

  let profileCards =  Array.from(
    document.getElementsByClassName("top-profiles-card")
  );

  let profileSection = document.getElementById('top-profiles')
  let revewsSection = document.getElementById('latest-reviews')

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