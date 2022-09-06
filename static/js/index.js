document.addEventListener("DOMContentLoaded", function () {
  let reviewCards = Array.from(
    document.getElementsByClassName("latest-reviews-card")
  );

  let profileCards =  Array.from(
    document.getElementsByClassName("top-profiles-card")
  );

  applyTransition(profileCards)
  applyTransition(reviewCards)

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
