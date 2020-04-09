import requests
from bs4 import BeautifulSoup as bf

response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
soup = bf(response.content, 'html.parser')

table = soup.find('table', { 'class' : 'table_develop3'})
data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])

print(data)

with open('weather.csv', 'w') as file:
    file.write('point,temperature,humidity\n')
    for i in data:
        file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2]))

