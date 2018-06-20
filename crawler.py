#Crawler da caculadepneus
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


URLs = [
    "http://www.caculadepneus.com.br/loja/catalogsearch/result/?order=price&dir=asc&q=225%2F55R18",
    "http://www.caculadepneus.com.br/loja/catalogsearch/result/?order=price&dir=asc&q=225%2F60R16",
    "http://www.caculadepneus.com.br/loja/catalogsearch/result/?order=price&dir=asc&q=225%2F65R17"
]
url = "http://www.caculadepneus.com.br/loja/catalogsearch/result/?order=price&dir=asc&q=225%2F55R18"
hdr = {'User-Agent': 'Mozilla/5.0'}

req = Request(url, headers=hdr)
page  = urlopen(req).read()
soup = BeautifulSoup(page, "html.parser")

precos_pneus = soup('span', {'itemprop': 'price'})
print(precos_pneus)

with open("dados.txt", "a+") as file:
    for item in precos_pneus:
        file.write(str(item))

#precisamos da descrição desse item no site, o site pesquisado e o preço do item encontrado.