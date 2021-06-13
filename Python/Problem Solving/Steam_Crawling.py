import requests
from bs4 import BeautifulSoup
import ssl
import pymysql
import re

conn = pymysql.connect(host="localhost",
                       user="project",
                       password="project",
                       db="project",
                       charset="utf8")
cur = conn.cursor()
url = "https://store.steampowered.com/search/?l=koreana"
res = requests.get(url)
res.raise_for_status()
soup_list = BeautifulSoup(res.text, "lxml")  # 모든 태그 가져오기
secondCount = 1
# 큰 리스트 가져오기 (div태그에 해당 id를 가진 애들)
news = soup_list.find("div", attrs={"id": "search_resultsRows"})

# 할인율
sales = soup_list.select(
   "div.responsive_search_name_combined > "
   "div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow ")
sales = map(str, sales)
sale_list = []
for sale in sales:
    sale = re.findall(r'[\d]+', sale)
    if sale:
        sale_list.append(sale[0])
    else:
        sale_list.append("0")

unv_context = ssl._create_unverified_context()

# 각 게임당 접속
for idx, a in enumerate(news.select("a", attrs={"class": "search_result_row ds_collapse_flag  app_impression_tracked"})):

    code = a.get('data-ds-appid')
    if not code:
        continue
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

    # 게임 이미지

    inImage = soup.select_one("#gameHeaderImageCtn > img")['src']
    print("게임 이미지: " + inImage)

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
    inDate = re.findall(r'[\d]+', inDate)
    inDate = "-".join(inDate)
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
        inPrice = "가격 확인이 불가한 게임입니다."
    else:
        inPrice = ainPrice.get_text().strip()
        if not inPrice == "무료" or "Free" in inPrice:
            inPrice = inPrice[2:].split(",")
            inPrice = "".join(inPrice)
        else:
            inPrice = "무료"

    # 성인게임의 경우
    if ainPrice is None:
        inPrice = "가격 확인이 불가한 게임입니다."
    else:
        inPrice = ainPrice.get_text().strip()
        if not inPrice == "무료" or "Free" in inPrice:
            inPrice = inPrice[2:].split(",")
            inPrice = "".join(inPrice)
        else:
            inPrice = "무료"

    print("게임 가격: ", inPrice)

    #게임 태그
    inTag = soup.select("#game_highlights > div.rightcol > div > div.glance_ctn_responsive_right > div.glance_tags_ctn.popular_tags_ctn > div.glance_tags.popular_tags > a")
    tagList = []
    for i, tag in enumerate(inTag):
        tagList.append(tag.text.strip())
    print("게임 태그: " + ", ".join(tagList))

    # STEAM 리스트 사진 큰 것
    # images = soup.select("#highlight_player_area > div.highlight_player_item.highlight_screenshot > div.screenshot_holder > a.highlight_screenshot_link")
    # for img in images:
    #     print(img['href'])

    # 사진이 너무 작음
    # images = soup.select("#highlight_strip_scroll > div.highlight_strip_item.highlight_strip_screenshot > img")
    # for img in images:
    #     print(img['src'])

    lst = [inTitle, inImage, inPrice, inContent, tagList[0], ", ".join(tagList), inDate, sale_list[idx]]
    try:
        print(lst)
        sql = "INSERT INTO game(gameName, gameImage, gamePrice, gameContent, gameCategory, gameGenre, gameReleasedDate, discountRate)" \
              "VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
        cur.execute(sql, lst)

    except Exception as e:
        try:
            sql = """UPDATE game 
                  SET discountRate = %s 
                  WHERE gameName = %s
                  """
            cur.execute(sql, sale_list[idx])
            cur.execute(sql, inTitle)
        except:
            print("========================================")
            print("에러 발생!", e)
            print(idx, inTitle, inImage, inPrice, inContent)
            print(", ".join(tagList), inDate)
conn.commit()
conn.close()
