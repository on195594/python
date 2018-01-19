import urllib.request

request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
html = response.read().decode('utf8')
print(html)
