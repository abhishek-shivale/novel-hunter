from urllib.parse import urlparse
import cloudscraper
import re

def get_scraper():
    return cloudscraper.create_scraper()


main = "https://ranobes.top"


def getImage(poster_style):
    start = poster_style.find("background-image: url('") + len(
        "background-image: url('"
    )
    end = poster_style.find(")", start)
    poster = poster_style[start:end]
    return poster


novel_ranking_list = {
    "Monthly": {
        "Rating": "https://ranobes.top/ranking/rated/month",
        "Comments": "https://ranobes.top/ranking/commented/month",
        "Views": "https://ranobes.top/ranking/month",
        "Bookmarks": "https://ranobes.top/ranking/bookmarks/month",
        "Chapters": "https://ranobes.top/ranking/chapters/month",
    },
    "Season": {
        "Rating": "https://ranobes.top/ranking/rated",
        "Comments": "https://ranobes.top/ranking/commented",
        "Views": "https://ranobes.top/ranking",
        "Bookmarks": "https://ranobes.top/ranking/bookmarks",
        "Chapters": "https://ranobes.top/ranking/chapters",
    },
    "Semi_annual": {
        "Rating": "https://ranobes.top/ranking/rated/bi_annual",
        "Comments": "https://ranobes.top/ranking/commented/bi_annual",
        "Views": "https://ranobes.top/ranking/bi_annual",
        "Bookmarks": "https://ranobes.top/ranking/bookmarks/bi_annual",
        "Chapters": "https://ranobes.top/ranking/chapters/bi_annual",
    },
    "Annual": {
        "Rating": "https://ranobes.top/ranking/rated/annual",
        "Comments": "https://ranobes.top/ranking/commented/annual",
        "Views": "https://ranobes.top/ranking/annual",
        "Bookmarks": "https://ranobes.top/ranking/bookmarks/annual",
        "Chapters": "https://ranobes.top/ranking/chapters/annual",
    },
    "Bi_annual": {
        "Rating": "https://ranobes.top/ranking/rated/two_years",
        "Comments": "https://ranobes.top/ranking/commented/two_years",
        "Views": "https://ranobes.top/ranking/two_years",
        "Bookmarks": "https://ranobes.top/ranking/bookmarks/two_years",
        "Chapters": "https://ranobes.top/ranking/chapters/two_years",
    },
    "All_time": {
        "Rating": "https://ranobes.top/ranking/rated/all_time",
        "Comments": "https://ranobes.top/ranking/commented/all_time",
        "Views": "https://ranobes.top/ranking/all_time",
        "Bookmarks": "https://ranobes.top/ranking/bookmarks/all_time",
        "Chapters": "https://ranobes.top/ranking/chapters/all_time",
    },
}


def generate_new_url(input_url):
    # Parse the input URL
    parsed_url = urlparse(input_url)

    # Extract the path from the parsed URL
    path = parsed_url.path

    # Get the base URL (host)
    host = parsed_url.scheme + "://" + parsed_url.netloc

    # Combine the host with the path
    new_url = path

    return new_url


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Brave\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
}


def extract_chapter_number(chapter_title):
    match = re.match(r'Chapter (\d+)', chapter_title)
    if match:
        return int(match.group(1)) 
    else:
        return None