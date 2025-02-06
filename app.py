from flask import Flask, request, jsonify
from scrapper.home import home
from scrapper.top_novel import get_top_novel
from scrapper.novel_info import get_novel_info
from scrapper.novel_chapters_list import get_novel_chapters_list
from scrapper.nove_chapter_info import get_novel_chapter_info
from utils.utils import novel_ranking_list, main

app = Flask(__name__)


@app.route("/")
def novel_home():
    try:
        home_content = home()
    except:
        home_content = "error"
    return home_content


@app.route("/novel")
def get_top_novel_list():
    novel_time = request.args.get("time")
    novel_type = request.args.get("type")

    if not novel_time or not novel_type:
        return {
            "status": "error",
            "message": "time and type are required",
            "hint": {
                "time": (
                    list(novel_ranking_list.keys())
                    if novel_ranking_list
                    else novel_ranking_list.keys()
                ),
                "type": (
                    list(novel_ranking_list["Monthly"].keys())
                    if novel_ranking_list
                    else novel_ranking_list["Monthly"].keys()
                ),
            },
        }

    try:
        novel_content = get_top_novel(novel_ranking_list[novel_time][novel_type])
    except Exception as e:
        novel_content = f"Error: {str(e)} {novel_content}"

    return novel_content


@app.route("/novels/<url>")
def get_novel_info_list(url):
    if not url:
        return {
            "status": "error",
            "message": "url is required",
        }
    full_url = main + "/novels/" + url
    try:
        novel_content = get_novel_info(full_url)
    except Exception as e:
        novel_content = f"Error: {str(e)} {novel_content}"
    return novel_content


@app.route("/chapters/<url>/<number>")
def get_chapters_list(url, number):
    if not url or not number:
        return {
            "status": "error",
            "message": "url and number is required",
            "hint": {"url": "/chapters/your_url/your_number"},
        }
    full_url = main + "/chapters/" + url
    try:
        novel_content = get_novel_chapters_list(full_url, number)
    except Exception as e:
        novel_content = f"Error: {str(e)} {novel_content}"
    return novel_content


@app.route("/info/<url>/<id>")
def get_chapter_info(url, id):
    if not url or not id:
        return {
            "status": "error",
            "message": "url and id is required",
            "hint": {"url": "/info/your_url/your_id"},
        }
    full_url = main + "/" + url + "/" + id
    try:
        novel_content = get_novel_chapter_info(full_url)
    except Exception as e:
        novel_content = f"Error: {str(e)} {novel_content}"
    return jsonify(novel_content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)