import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import ssl
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="root", db="pythonDB", charset="utf8")
cur = conn.cursor()
url = "https://store.steampowered.com/search/?l=koreana"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")  # 모든 태그 가져오기
idx = 0
secondCount = 1
# 큰 리스트 가져오기 (div태그에 해당 id를 가진 애들)
news = soup.find("div", attrs={"id": "search_resultsRows"})
gameGenre = []  # 게임 장르 배열


unv_context = ssl._create_unverified_context()

# 각 게임당 접속
for a in news.select("a", attrs={"class": "search_result_row ds_collapse_flag  app_impression_tracked"}):

    code = a.get('data-ds-appid')
    newUrl = "https://store.steampowered.com/app/"+code+"/?l=koreana"

    # 몇번째 게임인지 표시
    print("===============", idx+1, "번째 게임입니다.===============")
    print("game_code: ", code)
    # print(a) #해당 게임 전체 태그 (a태그)

    # 각 게임마다의 url 가지고 오기 + #?l=korean 을 통해 한국어 언어 설정
    urlSearch = newUrl
    print("urlSearch: "+urlSearch)

    # 해당 url를 가지고 새로운 웹사이트로 들어가기 (2번째 bs4 시작)
    res = requests.get(urlSearch)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # 게임 타이틀 이름
    ainTitle = soup.find(
        "div", attrs={"class": "apphub_AppName"})
    inTitle = ainTitle.get_text()
    print("게임 이름: ", inTitle)

    # # 게임 이미지 -> img 현04/24 확인, 막힘 (403 Forbidden)
    # ainImage = soup.find(
    #     "img", attrs={"class": "game_header_image_full"})
    # imgUrl = ainImage.get('src')
    # r = requests.get(imgUrl, stream=True)
    # if r.status_code == 200:
    #     print(r.status_code)
    #     with urllib.request.urlopen(imgUrl) as f:
    #         with open('./img/'+inTitle+'.jpg', 'wb') as h:
    #             ainImage = f.read()
    #             h.write(ainImage)

    # 게임 타이틀 내용/요약
    inContent = soup.find("div", attrs={"class": "game_description_snippet"})
    if inContent is None:
        inContent = "관련 설명이 없습니다."
    else:
        inContent = inContent.get_text().strip()
    print("게임 설명: ", inContent)

    # 게임 출시일
    ainDate = soup.find("div", attrs={"class": "date"})
    inDate = ainDate.get_text().strip()
    print("게임 출시일: ", inDate)

    # 게임 가격
    ainPrice = soup.select_one(
        "div.game_purchase_action > div > div.discount_block.game_purchase_discount > div.discount_prices > div.discount_original_price")
    if ainPrice is None:
        ainPrice = soup.select_one(
            "div.game_area_purchase_game_wrapper > div >  div.game_purchase_action > div >  div.game_purchase_price.price")
    if ainPrice is None:
        ainPrice = soup.select_one(
            "#game_area_purchase > div.game_area_purchase_game > div.game_purchase_action > div > div.game_purchase_price.price")
    if ainPrice is None:
        inPrice = "가격확인이 불가하거나 이미 소지한 게임입니다."
    else:
        inPrice = ainPrice.get_text().strip()

    if ainPrice is None:
        inPrice = "가격확인 불가"
    else:
        inPrice = ainPrice.get_text().strip()

    print("게임 가격: ", inPrice)

    #게임 태그
    inTag = soup.select("#game_highlights > div.rightcol > div > div.glance_ctn_responsive_right > div.glance_tags_ctn.popular_tags_ctn > div.glance_tags.popular_tags > a")
    tagList = []
    for i, tag in enumerate(inTag):
        tagList.append(tag.text.strip())
    print("게임 태그: " + ", ".join(tagList))

    #게임 이미지
    # 사진 큰 것
    images = soup.select("#highlight_player_area > div.highlight_player_item.highlight_screenshot > div.screenshot_holder > a.highlight_screenshot_link")
    for img in images:
        print(img['href'])

    # 사진이 너무 작음
    # images = soup.select("#highlight_strip_scroll > div.highlight_strip_item.highlight_strip_screenshot > img")
    # for img in images:
    #     print(img['src'])


    idx += 1
    # try:
    #     sql = "INSERT INTO game(gameNo, gameName, gameImage, gamePrice, gameContent, gameCategory, genreGenre, gameReleasedDate)" \
    #           "VALUES(" + idx + ", " + "a" + ", " + inTitle + ", " + inPrice + ", " + inContent + ", " + game