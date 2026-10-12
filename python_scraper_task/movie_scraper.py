import requests
from bs4 import BeautifulSoup

movies_link = "https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s"

def scrape_movies():

    headers = {"User-Agent": "Mozilla/5.0"}
    result = requests.get(movies_link,headers=headers, timeout=10)
    result.raise_for_status()

    soup = BeautifulSoup(result.text, "lxml")
    movie_items = soup.select("table.wikitable")
    movies = []

    for movie in movie_items:
        rows = movie.select("tr")
        for row in rows[1:]:
            columns = row.select("td")

            if len(columns) >= 4:
                title = columns[0].get_text(strip=True)
                director = columns[1].get_text(strip=True)
                country = columns[3].get_text(strip=True)

                movies.append({"Title": title, "Director": director, "Country": country})
    return movies