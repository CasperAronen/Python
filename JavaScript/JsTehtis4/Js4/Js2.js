const form = document.getElementById('searchForm');

form.addEventListener('submit', e => {
    e.preventDefault();

    const query = document.getElementById('query').value;

    fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            console.log("Search results:", data);
        })
        .catch(err => console.error("Error fetching data:", err));
});