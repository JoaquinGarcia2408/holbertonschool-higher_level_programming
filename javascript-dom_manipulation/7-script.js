var listMovies = document.getElementById("list_movies");
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    data.results.forEach(element => {
        let newItem = document.createElement("li");
        li.textContent = movie.title;
        listMovies.appendChild(li);
    });
});