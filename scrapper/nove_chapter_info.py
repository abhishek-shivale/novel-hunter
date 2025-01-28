from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()


def get_novel_chapter_info(url):
  file = scraper.get(url).text
  elements = BeautifulSoup(file, "html.parser")

  page = elements.select_one('.str_left .shortstory ')

  title = page.select_one('.title').text.strip()
  content_parsed = page.select_one('#arrticle').text.strip()
  content_unparsed = page.select_one('#arrticle')
  return {
    "title" : title,
    "content_parsed" : content_parsed,
    "content_unparsed" : content_unparsed
  }
