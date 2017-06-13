from bs4 import BeautifulSoup as bs
import urllib.request

req = urllib.request.urlopen('https://www.nationaljournal.com/politics?rss=1')

xml = bs(req, 'xml')

for item in xml.findAll('link')[3:]:
    print(item.text)