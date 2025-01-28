from bs4 import BeautifulSoup
from utils.utils import getImage, get_scraper

def home():
    scraper = get_scraper()
    file = scraper.get("https://ranobes.top").text

    elements = BeautifulSoup(file, "html.parser")

    left_page = elements.select('#mainside > div.str_left > article')

    trending_novel = []

    for i in range(len(left_page)):
        value = left_page[i]
        title = value.select_one('.title').text
        poster = getImage(value.select_one('figure')['style'])
        link = value.select_one('.poster')['href']
        current_rating = value.select_one('.current-rating').text
        syspnosis = value.select_one('.cont-in > div').text.strip()
        genre = value.select_one('.grey').text.strip()

        trending_novel.append({
            "title": title,
            "poster": poster,
            "link": link,
            "current_rating": current_rating,
            "syspnosis": syspnosis,
            "genre": genre,
        })

    best_novel = []
    right_page = elements.select_one('#rightside > div > div')
    best_novel_pannel = right_page.select('#news_top > div')

    for i in range(len(best_novel_pannel)):
        value = best_novel_pannel[i]
        title = value.select_one('.title').text
        poster = getImage(value.select_one('i')['style'])
        rating = value.select_one('span.meta.opacity_5 > span').text
        link = value.select_one('a')['href']
        best_novel.append({
            "title": title,
            "poster" : poster,
            "rating": rating,
            "link": link
        })

    most_discussed = []
    most_discussed_pannel = right_page.select('#news_coms > div')
    for i in range(len(most_discussed_pannel)):
        value = most_discussed_pannel[i]
        title = value.select_one('.title').text
        poster = getImage(value.select_one('i')['style'])
        length = value.select_one('a > div > span.small.subtitle.ellipses').text
        link = value.select_one('a')['href']
        most_discussed.append({
            "title": title,
            "poster" : poster,
            "length": length,
            "link": link
        })

    return {
        "trending_novel": trending_novel,
        "best_novel": best_novel,
        "most_discussed_novel": most_discussed
    }