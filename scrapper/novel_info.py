from bs4 import BeautifulSoup
import cloudscraper
from utilis.utils import main
scraper = cloudscraper.create_scraper()


def get_novel_info(url):
  file = scraper.get(url).text
  elements = BeautifulSoup(file, "html.parser")

  page = elements.select_one('#dle-content > article > div.structure.str_fullview > div.str_left')

  title = page.select_one('.title').text.strip()

  content_small = page.select_one('.moreless__short').text

  content_full = page.select_one('.moreless__full').text

  details = page.select_one('.r-fullstory-spec > ul')

  banner =  main + page.select_one('.highslide > img')["src"]

  novel_info = {
      'Status_in_COO': details.select_one('li:nth-child(6) > span > a').text,
      'Translation':details.select_one('li:nth-child(7) > span > a').text ,
      'In_original': details.select_one('li:nth-child(8) > a').text,
      'Translated':details.select_one('li:nth-child(9) > span').text ,
      'Year_of_publishing': details.select_one('li:nth-child(10) > span > a').text,
      'Language': details.select_one('li:nth-child(11) > span > a').text,
      'Authors': details.select_one('li:nth-child(12) > span > a').text,
      'Translator': details.select_one('li:nth-child(13) > span > a').text,
      'Views': elements.select_one('ul:nth-child(2) > li:nth-child(1) > span').text,
      'Total_views': elements.select_one(' ul:nth-child(2) > li:nth-child(2) > span').text,
      'Comments': elements.select_one('#dle-comm-link').text,
      'Total_comments': elements.select_one('ul:nth-child(3) > li:nth-child(2) > span').text,

  }

  more_chapter = main + page.select('.r-fullstory-chapters-foot > .uppercase')[1]['href']

  return {
    'title': title,
    'content_small': content_small,
    'content_full': content_full,
    'banner': banner,
    'novel_info': novel_info,
    'more_chapter': more_chapter
  }