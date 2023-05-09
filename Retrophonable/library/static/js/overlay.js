function openOverlay(gameId) {
    var overlay = document.getElementById("overlay");
    var content = overlay.querySelector(".content");
    var gameDetailsUrl = "{% url 'library:GameDetails' 0 %}".replace("0", gameId);

    // Make an AJAX call to fetch the details of the game
    var xhr = new XMLHttpRequest();
    xhr.open("GET", gameDetailsUrl);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Populate the overlay with the game details
            var game = JSON.parse(xhr.responseText);
            content.querySelector(".title").textContent = game.title_text;
            content.querySelector(".console").textContent = game.console_text;
            content.querySelector(".category").textContent = game.category_text;
            content.querySelector(".multiplayer").textContent = game.multiplayer;
            overlay.style.display = "block";
        } else {
            console.log("Error fetching game details");
        }
    };
    xhr.send();
}
function closeOverlay() {
  document.getElementById("overlay").style.display = "none";
}