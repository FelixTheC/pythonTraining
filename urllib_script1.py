import urllib.request
import urllib.parse


values = {'q':'python programming tutorials'}
data = urllib.parse.urlencode(values)
#data = data.encode('utf-8') - if request method not allowed

url = 'https://www.google.com/search?'+data

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)



