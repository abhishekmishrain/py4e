import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_566298.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags

count = 0
sum = 0

tags = soup('span')
for tag in tags:
    #print("References: ", tag.get('href', None))
    #print("Contents: ", tag.contents)
    #print("Attributes: ", tag.attrs)
    count = count + 1
    sum = sum + int(tag.contents[0])

print("Count ", count)
print("Sum ", sum)
