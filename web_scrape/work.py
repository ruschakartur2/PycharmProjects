import requests
import codecs

from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {
    'User-Agent': 'Mozila/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 FIREFOX/47.0',
    'Accept': 'text/html,aplication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

base_url = 'https://www.work.ua/jobs-kyiv-python/'

domain = 'https://www.work.ua'
jobs = []
urls = []
urls.append(base_url)

req = session.get(base_url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content,"html.parser")
    pagination = bsObj.find('ul', attrs={'class': 'pagination'})
    if pagination:
        pages = pagination.findAll('li', attrs = {'class' : False})
        for page in pages:
            urls.append(domain + page.a['href'])


handle = codecs.open('div_list.html', "w")
handle.write(str(urls))
handle.close()
