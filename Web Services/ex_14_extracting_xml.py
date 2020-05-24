import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_566300.xml'

xml = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved ', len(xml), ' characters')
tree = ET.fromstring(xml)
namelist = tree.findall('comments/comment')
print('Count: ', len(namelist))
sum = 0
for name in namelist:
    #print('Name: ', name.find('name').text)
    #print('Count: ', name.find('count').text)
    sum = sum + int( name.find('count').text)

print('Sum: ', sum)
