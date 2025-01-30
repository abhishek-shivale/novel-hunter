from bs4 import BeautifulSoup
import cloudscraper
from utils.utils import main, generate_new_url, extract_chapter_number

scraper = cloudscraper.create_scraper()


def get_novel_info(url):
    file = scraper.get(url).text
    elements = BeautifulSoup(file, "html.parser")

    page = elements.select_one(
        "#dle-content > article > div.structure.str_fullview > div.str_left"
    )

    title = (
        page.select_one(".title").text.strip()
        if page.select_one(".title").text.strip()
        else ""
    )

    content_small = (
        page.select_one(".moreless__short").text
        if page.select_one(".moreless__short").text
        else ""
    )

    content_full = (
        page.select_one(".moreless__full").text
        if page.select_one(".moreless__full").text
        else ""
    )

    details = (
        page.select_one(".r-fullstory-spec > ul")
        if page.select_one(".r-fullstory-spec > ul")
        else ""
    )

    banner = main + page.select_one(".highslide > img")["src"]

    novel_info = {
        "Status_in_COO": (
            details.select_one("li:nth-child(6) > span > a").text
            if details.select_one("li:nth-child(6) > span > a")
            else ""
        ),
        "Translation": (
            details.select_one("li:nth-child(7) > span > a").text
            if details.select_one("li:nth-child(7) > span > a")
            else ""
        ),
        "In_original": (
            details.select_one("li:nth-child(8) > a").text
            if details.select_one("li:nth-child(8) > a")
            else ""
        ),
        "Translated": (
            details.select_one("li:nth-child(9) > span").text
            if details.select_one("li:nth-child(9) > span")
            else ""
        ),
        "Year_of_publishing": (
            details.select_one("li:nth-child(10) > span > a").text
            if details.select_one("li:nth-child(10) > span > a")
            else ""
        ),
        "Language": (
            details.select_one("li:nth-child(11) > span > a").text
            if details.select_one("li:nth-child(11) > span > a")
            else ""
        ),
        "Authors": (
            details.select_one("li:nth-child(12) > span > a").text
            if details.select_one("li:nth-child(12) > span > a")
            else ""
        ),
        "Translator": (
            details.select_one("li:nth-child(13) > span > a").text
            if details.select_one("li:nth-child(13) > span > a")
            else ""
        ),
        "Views": (
            elements.select_one("ul:nth-child(2) > li:nth-child(1) > span").text
            if elements.select_one("ul:nth-child(2) > li:nth-child(1) > span")
            else ""
        ),
        "Total_views": (
            elements.select_one(" ul:nth-child(2) > li:nth-child(2) > span").text
            if elements.select_one(" ul:nth-child(2) > li:nth-child(2) > span")
            else ""
        ),
        "Comments": (
            elements.select_one("#dle-comm-link").text
            if elements.select_one("#dle-comm-link")
            else ""
        ),
        "Total_comments": (
            elements.select_one("ul:nth-child(3) > li:nth-child(2) > span").text
            if elements.select_one("ul:nth-child(3) > li:nth-child(2) > span")
            else ""
        ),
    }

    more_chapter = (
        main + page.select(".r-fullstory-chapters-foot > .uppercase")[1]["href"]
    )

    chapters = elements.select_one('.chapters-scroll-list > li')

    latest_chapter = chapters.select_one('.ellipses').text


    return {
        "title": title,
        "content_small": content_small,
        "content_full": content_full,
        "banner": banner,
        "novel_info": novel_info,
        "more_chapter": generate_new_url(more_chapter) + '1',
        "latest_chapter": extract_chapter_number(latest_chapter)
    }
