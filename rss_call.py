import requests
import bs4

'''request url using a web browser header'''
url = 'https://thenextweb.com/plugged/feed/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r = requests.get(url, headers=headers)

'''parse the html using beautiful soup'''
soup = bs4.BeautifulSoup(r.text, 'html.parser')

for item in soup.find_all('item'):
    print(item.title.text)
    print(item.link)
    print(item.description.ahref)
    print(item.pubdate)

'''extract article url links'''
for link in soup.find_all('link'):
    print(link.text)




