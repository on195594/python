# coding:utf-8

import requests
from bs4 import BeautifulSoup

url = "https://www.douban.com/group/148995/"
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,"html5lib")
# print (soup)
new_title = soup.select("td.title > a")
# print(new_title)
for i in new_title:
    title = i.get_text()
    link = i.get("href")
    data = {
    "标题":title,
    "链接":link
    }
    print (data)