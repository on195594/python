# coding:utf-8

import requests
import json

url = "https://www.toutiao.com/api/pc/focus/"
webdata = requests.get(url).text

data = json.loads(webdata)
news = data['data']['pc_feed_focus']
# print(news)

for n in news:
    title = n['title']
    image_url = n['image_url']
    url = "https://www.toutiao.com"+n['display_url']
    print (url,title,image_url)