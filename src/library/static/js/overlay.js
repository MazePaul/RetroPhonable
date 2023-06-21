const overlay = document.querySelector('.overlay');

// Hide the overlay when the user clicks outside of it
overlay.addEventListener('click', (event) => {
    if (event.target === overlay) {
        overlay.style.display = 'none';
    }
});

//creation de la fonction pour passer les détails des jeux
function openOverlay(gameId, url) {
  var gameIdInput = overlay.querySelector("#game-id");
  var titleText = overlay.querySelector("#game-title");
  var consoleText = overlay.querySelector("#game-console");
  var categoryText = overlay.querySelector("#game-category");
  var multiplayerText = overlay.querySelector("#game-multiplayer");
  var coverText = overlay.querySelector("#game-cover");

  var bool = "";

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
      if (gameData.multiplayer == false){
        bool = "non"
      }else{
        bool = "oui"
      }
      multiplayerText.innerHTML = bool;
      coverText.src = gameData.cover;
      overlay.style.display = "block";

      coverText.style.width = 'auto';
      coverText.style.height = '300px';
    }
  };
  //xhr.open('GET', `game/${gameId}/`);
  //On check si c'est search ou non (url non vide = search)
  if (url){
    xhr.open('GET', `${gameId}/`);
    xhr.send();
  }else{
    xhr.open('GET', `search/${gameId}/`);
    xhr.send();
  }
}

function determineUrl(gameId){
    var url=window.location.pathname;
    let bool="";
    if (url.includes("search/")){
        bool = "search/";
        openOverlay(gameId, bool);
    }else{
        openOverlay(gameId, bool);
    }
}