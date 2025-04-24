from bs4 import BeautifulSoup
import cloudscraper
from utils.utils import generate_new_url


def get_top_novel(url):
    scraper = cloudscraper.create_scraper()
    file = scraper.get(url).text

    elements = BeautifulSoup(file, "html.parser")

    page = elements.select("#ranking-content > article")

    top_novel = []

    for i in range(len(page)):
        value = page[i]
        title = value.select_one(".title").text
        short_content = value.select_one(".moreless__short").text
        full_content = value.select_one(".moreless__full").text
        link = value.select_one(".title > a")["href"]
        # current_rating = value.select_one('.current-rating').text or ""
        genre = value.select_one(".grey").text.strip()

        top_novel.append(
            {
                "title": title,
                "short_content": short_content,
                "full_content": full_content,
                "link": generate_new_url(link),
                "genre": genre,
            }
        )
    return top_novel
