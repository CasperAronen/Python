const form = document.getElementById('searchForm');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', e => {
    e.preventDefault();

    const query = document.getElementById('query').value;

    resultsDiv.innerHTML = '';

    fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            data.forEach(tvShow => {
                const show = tvShow.show;

                const article = document.createElement('article');
                article.classList.add('card');

                const h2 = document.createElement('h2');
                h2.textContent = show.name;
                article.appendChild(h2);

                const link = document.createElement('a');
                link.href = show.url;
                link.textContent = "More details";
                link.target = "_blank";
                article.appendChild(link);

                if (show.image?.medium) {
                    const img = document.createElement('img');
                    img.src = show.image.medium;
                    img.alt = show.name;
                    article.appendChild(img);
                }

                const summaryDiv = document.createElement('div');
                summaryDiv.innerHTML = show.summary || "No summary available";
                article.appendChild(summaryDiv);

                resultsDiv.appendChild(article);
            });
        })
        .catch(err => console.error("Error fetching data:", err));
});
