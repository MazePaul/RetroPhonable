const overlay = document.querySelector('.overlay');

// Hide the overlay when the user clicks outside of it
overlay.addEventListener('click', (event) => {
    if (event.target === overlay) {
        overlay.style.display = 'none';
    }
});

//creation de la fonction pour passer les détails des jeux
function openOverlay(gameId) {
  var gameIdInput = overlay.querySelector("#game-id");
  var titleText = overlay.querySelector("#game-title");
  var consoleText = overlay.querySelector("#game-console");
  var categoryText = overlay.querySelector("#game-category");
  var multiplayerText = overlay.querySelector("#game-multiplayer");

  // Set the value of the hidden input field
  gameIdInput.value = gameId;

  //API calls to
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      const gameData = JSON.parse(xhr.responseText);

      // populate the overlay
      titleText.innerHTML = gameData.title;
      consoleText.innerHTML = gameData.console;
      categoryText.innerHTML = gameData.category;
      multiplayerText.innerHTML = gameData.multiplayer;
      overlay.style.display = "block";

      console.level = 'debug'
      console.log(gameData);
    }
  };
  xhr.open('GET', `game/${gameId}/`);
  xhr.send();
}