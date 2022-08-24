import requests
import bs4
from headers import HEADERS

KEYWORDS = ['Сегодня', 'сегодня', 'пришлось']
tag_1 = "article-formatted-body article-formatted-body article-formatted-body_version-1"
tag_2 = "article-formatted-body article-formatted-body article-formatted-body_version-2"

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('div', class_="tm-article-snippet")

for article in articles:
    article_date = article.find('time').attrs['title']
    href = article.find('a').attrs['href']
    article_name = article.find('h2')
    url = 'https://habr.com' + href

    hubs_1 = article.find_all('div', class_=tag_1)
    for hub in hubs_1:
        for keyword in KEYWORDS:
            if keyword in hub.text:
                print(f'По слову "{keyword}" найдено: {article_date}-->{article_name.text}-->{url}')

    hubs_2 = article.find_all('div', class_=tag_2)
    for hub in hubs_2:
        for keyword in KEYWORDS:
            if keyword in hub.text:
                print(f'По слову "{keyword}" найдено: {article_date}-->{article_name.text}-->{url}')
