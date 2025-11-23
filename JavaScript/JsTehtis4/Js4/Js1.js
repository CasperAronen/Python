const form = document.getElementById('searchForm');
form.addEventListener('submit', e => {

    const query = document.getElementById('query').value;

    fetch(`https://api.tvmaze.com/singlesearch/shows?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
            console.log("Title:", data.name);
            console.log("Genres:", data.genres.join(", "));
            console.log("Premiered:", data.premiered);
            console.log("Rating:", data.rating.average);
            console.log("Summary:", data.summary.replace(/<[^>]+>/g, ""));
        })
        .catch(err => console.error(err));
});
