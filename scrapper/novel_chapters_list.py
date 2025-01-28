from bs4 import BeautifulSoup
import re
import cloudscraper
import json



def getFile (main, number):
    scraper = cloudscraper.create_scraper()
    url = f"{main}/page/{number}" if number >= 2 else f"{main}"
    print(url)
    return scraper.get(url).text

def get_novel_chapters_list(main, number):


  file = getFile(main, number)

  elements = BeautifulSoup(file, "html.parser")

  page = elements.select_one('.str_left')

  chapters = page.select_one('.cat_block')
  print(page)

  script_tag = page.find('script', string=re.compile(r'window\.__DATA__'))


  script_content = script_tag.string

  match = re.search(r'window\.__DATA__\s*=\s*({.*})', script_content)

  json_data = json.loads(match.group(1))

  book_title = json_data["book_title"]

  book_link = json_data["book_link"]

  book_id = json_data["book_id"]

  chapters = json_data['chapters']

  return {
     "book_title": book_title,
     "book_link" : book_link,
     "book_id" : book_id,
     "chapters" : chapters
  }
