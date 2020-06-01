import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.3'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

for item in soup.select('table > tbody > .list'):
    rank = item.select_one('.number').text.split('\n')[0]
    title = item.select_one('.info > .title.ellipsis').text
    artist = item.select_one('.info > .artist.ellipsis').text
    if rank:    
         print(rank, title.strip(), artist.strip())
