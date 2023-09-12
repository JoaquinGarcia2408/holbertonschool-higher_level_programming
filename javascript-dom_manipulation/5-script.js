var updater = document.getElementById("update_header");
var head = document.querySelector("header");

updater.addEventListener("click", function() {
    head.textContent = "New Header!!!";
});