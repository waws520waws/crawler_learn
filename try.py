import requests
from lxml import etree

url = 'https://www.elespectador.com/mundo/mas-paises/biden-y-putin-hablaron-por-telefono-continuan-las-discusiones-por-ucrania-noticias-de-hoy/'

req = requests.get(url).text
page = etree.HTML(req)
tab_p = page.xpath('//*[@id="main-layout"]/section[1]/div[2]/div[2]/div[2]/section[1]/article/div[1]/section/p')

for p in tab_p:
    cnt = p.xpath('.//text()')

    print(cnt)