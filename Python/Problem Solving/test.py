import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_argument("--lang=ko")
prefs = {
    "translate_whitelists": {"en": "ko"},
    "translate": {"enabled": "true"}
}
option.add_experimental_option("prefs", prefs)
#option.add_argument("--headless")
url = "https://store.steampowered.com/search/"
path = "C:/Users/YangJi/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path, options=option)
#html = driver.find_element_by_tag_name("html")
#driver.execute_script('arguments[0].setAttribute("lang", "ko");', html)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
idx = 1
secondCount = 1
news = soup.find("div", attrs={"id": "search_resultsRows"})
gameGenre = []
for a in news.select("a", attrs={"class": "search_result_row ds_collapse_flag  app_impression_tracked"}):
    try:
        # index올라감
        print("===============", idx, "번째 게임입니다.===============")
        idx += 1

        # 각 게임마다의 url 가지고 오기
        urlSearch = a.get('href')

        # 해당 url를 가지고 새로운 웹사이트로 들어가기 (2번째 bs4 시작)
        driver.implicitly_wait(2)

        driver.get(urlSearch)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "lxml")

        # 게임 타이틀 이름
        ainTitle = soup.find("div", attrs={"class": "apphub_AppName"})
        inTitle = ainTitle.get_text()
        print("게임 이름: ", inTitle)

        # 게임 타이틀 내용/요약
        inContent = soup.find("div", attrs={"class": "game_description_snippet"})
        if inContent is None:
            inContent = "관련 설명이 없습니다."
        else:
            inContent = inContent.get_text().strip()
        print("게임 설명: ", inContent)

        # 게임 출시일
        ainDate = soup.find("div", attrs={"class": "date"})
        inDate = ainDate.get_text()
        print("게임 출시일: ", inDate)

        # 게임 태그 (5개까지만)
        for inGenre in soup.find_all("a", attrs={"class": "app_tag"}, limit=5):
            # print("게임 장르: ", inGenre.get_text().strip())
            singleGenre = inGenre.get_text().strip()
            gameGenre.append(singleGenre)
            secondCount = secondCount+1
            if len(gameGenre) == 5:
                csvFile = open('testfile.csv', 'a', encoding='UTF-8', newline='')
                writer = csv.writer(csvFile)
                print(gameGenre)
                try:
                    writer.writerow(('game_name', 'game_content',
                                     'game_date', "game_genre"))
                    writer.writerow((inTitle, inContent, inDate, gameGenre))
                finally:
                    csvFile.close()
                gameGenre.clear()
    except:
        print("성인게임 ㅠㅠ 이거 나중에 셀레늄으로 조작해보기")
        continue