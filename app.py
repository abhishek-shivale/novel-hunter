# from scrapper.home import home
# from scrapper.top_novel import *
from scrapper.novel_info import get_novel_info
from scrapper.novel_chapters_list import get_novel_chapters_list
from scrapper.nove_chapter_info import get_novel_chapter_info
# home()

# get novel_ranking_list url from novel_ranking_list from parametere
# print(get_top_novel())


# print(get_novel_info("https://ranobes.top/novels/133485-lord-of-the-mysteries-v812312.html"))

# print(get_novel_chapters_list('https://ranobes.top/chapters/1206735', 12))

url = "https://ranobes.top/lord-of-the-mysteries-v812312-133485/2067366.html"

print(get_novel_chapter_info(url))
