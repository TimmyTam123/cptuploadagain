document.addEventListener("DOMContentLoaded", function () {
  const infobut = document.getElementById("info");
  const thingy = document.getElementById("thingymabobby");

  infobut.addEventListener("click", function () {
    thingy.style.visibility = "show"; // Or 'flex', 'grid', etc.
  });
});
