import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Elias.html'

# Retrieve all of the span tags

count = int(input('Enter count: '))
position = int(input('Enter position: '))

while count >= 0:
    #print("References: ", tag.get('href', None))
    #print("Contents: ", tag.contents)
    #print("Attributes: ", tag.attrs)
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href', None)
    count = count - 1
