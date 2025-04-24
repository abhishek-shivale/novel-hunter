from urllib.parse import urlparse
import cloudscraper
import re

def get_scraper():
    return cloudscraper.create_scraper()


main = "https://ranobes.net"


def getImage(poster_style):
    start = poster_style.find("background-image: url('") + len(
        "background-image: url('"
    )
    end = poster_style.find(")", start)
    poster = poster_style[start:end]
    return poster


novel_ranking_list = {
    "Monthly": {
        "Rating": "https://ranobes.net/ranking/rated/month",
        "Comments": "https://ranobes.net/ranking/commented/month",
        "Views": "https://ranobes.net/ranking/month",
        "Bookmarks": "https://ranobes.net/ranking/bookmarks/month",
        "Chapters": "https://ranobes.net/ranking/chapters/month",
    },
    "Season": {
        "Rating": "https://ranobes.net/ranking/rated",
        "Comments": "https://ranobes.net/ranking/commented",
        "Views": "https://ranobes.net/ranking",
        "Bookmarks": "https://ranobes.net/ranking/bookmarks",
        "Chapters": "https://ranobes.net/ranking/chapters",
    },
    "Semi_annual": {
        "Rating": "https://ranobes.net/ranking/rated/bi_annual",
        "Comments": "https://ranobes.net/ranking/commented/bi_annual",
        "Views": "https://ranobes.net/ranking/bi_annual",
        "Bookmarks": "https://ranobes.net/ranking/bookmarks/bi_annual",
        "Chapters": "https://ranobes.net/ranking/chapters/bi_annual",
    },
    "Annual": {
        "Rating": "https://ranobes.net/ranking/rated/annual",
        "Comments": "https://ranobes.net/ranking/commented/annual",
        "Views": "https://ranobes.net/ranking/annual",
        "Bookmarks": "https://ranobes.net/ranking/bookmarks/annual",
        "Chapters": "https://ranobes.net/ranking/chapters/annual",
    },
    "Bi_annual": {
        "Rating": "https://ranobes.net/ranking/rated/two_years",
        "Comments": "https://ranobes.net/ranking/commented/two_years",
        "Views": "https://ranobes.net/ranking/two_years",
        "Bookmarks": "https://ranobes.net/ranking/bookmarks/two_years",
        "Chapters": "https://ranobes.net/ranking/chapters/two_years",
    },
    "All_time": {
        "Rating": "https://ranobes.net/ranking/rated/all_time",
        "Comments": "https://ranobes.net/ranking/commented/all_time",
        "Views": "https://ranobes.net/ranking/all_time",
        "Bookmarks": "https://ranobes.net/ranking/bookmarks/all_time",
        "Chapters": "https://ranobes.net/ranking/chapters/all_time",
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