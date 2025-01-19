import cloudscraper

def get_scraper():
    return cloudscraper.create_scraper()


def getImage(poster_style):
    start = poster_style.find("background-image: url('") + len("background-image: url('")
    end = poster_style.find(")", start)
    poster = poster_style[start:end]
    return poster