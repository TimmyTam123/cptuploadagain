document.addEventListener("DOMContentLoaded", function () {
  const showButton = document.getElementById("settings");
  const hiddenContent = document.getElementById("settingsov");
  const backbutton = document.getElementById("back");

  showButton.addEventListener("click", function () {
    hiddenContent.style.display = "flex"; // Or 'flex', 'grid', etc.
  });
  backbutton.addEventListener("click", function () {
    hiddenContent.style.display = "none"; // Or 'flex', 'grid', etc.
  });
});
