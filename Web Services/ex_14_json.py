import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.json'

jsonfile = urllib.request.urlopen(url, context=ctx).read().decode()

print('Retrieved ', len(jsonfile), ' characters')
#print(json)

info = json.loads(jsonfile)

sum = 0
count = 0
for item in info['comments']:
    #print(item)
    #print('Name: ', item['name'])
    #print('Name: ', item['count'])
    sum = sum + int(item['count'])
    count = count + 1;

print('Count: ', count)
print('Sum: ', sum)
