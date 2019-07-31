import requests
from bs4 import BeautifulSoup

url = "http://www.animeshow.tv/anime-list.html"
urllist = []
dm = open('dm.txt', 'a', encoding='utf-8')
def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
soup = BeautifulSoup(get_page(url), 'lxml')
data = soup.select('#anime_list > div > ul > li > a')
for item in data:
    result={
        'title': item.get_text(),
        'link' : item.get('href')
    }
    urllist.append(result['link'])

for item in urllist:
    html = requests.get(item).text
    soup2 = soup = BeautifulSoup(get_page(item), 'lxml')
    Genres1 = soup2.select('#anime > div.row > div.a_in > div:nth-child(4) > div:nth-child(2)')
    for item2 in Genres1:
        result1 = item2.get_text()

    name = soup2.select('#anime > h1')
    url = item
    type1 = soup2.select('#anime > div.row > div.a_in > div:nth-child(1) > div:nth-child(2)')
    year = soup2.select('#anime > div.row > div.a_in > div:nth-child(2) > div:nth-child(2)')
    Status = soup2.select('#anime > div.row > div.a_in > div:nth-child(3) > div:nth-child(2)')
    Genres = result1
    Summary = soup2.select('#anime > div.anime_discription > p')

    animes = {
        '动漫名称': name[0].get_text(),
        '动漫地址': url,
        '类型': type1[0].get_text(),
        '播出时间': year[0].get_text(),
        '状态': Status[0].get_text(),
        '流派': Genres,
        '摘要': Summary

    }
    print(animes,file=dm)
