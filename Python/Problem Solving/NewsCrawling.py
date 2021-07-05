import requests
from bs4 import BeautifulSoup
import pymysql


conn = pymysql.connect(host="localhost",
                       user="project",
                       password="project",
                       db="project",
                       charset="utf8")
url = 'https://www.gamemeca.com/news.php'
cur = conn.cursor()
res = requests.get(url)
res.raise_for_status()
news = BeautifulSoup(res.text, "lxml")
select_list = "#content > div.news-list > div.content-left > ul > li"
for i in news.select(select_list):
    a = i.select_one("div.cont_thumb_h > strong > a")
    if not a:
        a = i.select_one("div.cont_thumb > strong > a")
    date = i.select_one("div.day_news").text
    title = a.text
    link = "https://www.gamemeca.com/" + a['href']
    print(title, link, date)

    lst = [title, link, date]
    try:
        sql = "INSERT INTO news(newsTitle, newsUrl, newsDate)" \
              "VALUES(%s, %s, %s);"
        cur.execute(sql, lst)
    except Exception as e:
            print("========================================")
            print("에러 발생!", e)
conn.commit()
conn.close()
