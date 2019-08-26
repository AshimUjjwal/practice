import requests
import bs4

r=requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
soup = bs4.BeautifulSoup(r.text,'html5lib')
print(soup.select('a'))
