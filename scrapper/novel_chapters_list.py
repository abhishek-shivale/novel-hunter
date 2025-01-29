from bs4 import BeautifulSoup
import re
import cloudscraper
import json
from utils.utils import generate_new_url


def getFile(main, number):
    scraper = cloudscraper.create_scraper()
    url = f"{main}/page/{number}" if int(number) >= 2 else f"{main}"
    return scraper.get(url).text


def get_novel_chapters_list(main, number):

    file = getFile(main, number)

    elements = BeautifulSoup(file, "html.parser")

    page = elements.select_one(".str_left")

    script_tag = page.find("script", string=re.compile(r"window\.__DATA__"))

    script_content = script_tag.string

    match = re.search(r"window\.__DATA__\s*=\s*({.*})", script_content)

    json_data = json.loads(match.group(1))

    book_title = json_data["book_title"]

    book_link = json_data["book_link"]

    book_id = json_data["book_id"]

    chapters = json_data["chapters"]

    for chapter in chapters:
        chapter["link"] = "/info" + generate_new_url(chapter["link"])

    return {
        "book_title": book_title,
        "book_link": generate_new_url(book_link),
        "book_id": book_id,
        "chapters": chapters,
    }
