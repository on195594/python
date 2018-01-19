# coding:utf-8

import requests
from bs4 import BeautifulSoup
url = "https://www.douban.com/?p="
cookie = 'll="118209"; bid=QJWDmQWc2zw; _ga=GA1.2.1276413593.1495944664; __ads_session=LXy2R3w36wgmBOYtTQA=; __yadk_uid=95DoDFIVKU6Tnt9olc2aEySrRLItez9v; gr_user_id=44111cd4-9864-4f4c-9b22-69b28b66ba63; ue="isoul.lin@gmail.com"; ap=1; __utmc=30149280; __utmv=30149280.131; _vwo_uuid_v2=5A4F8863742C70054E7AA021EBF00ABF|c21118598b5bd8b950ea97484753c6a2; ps=y; ct=y; push_noty_num=0; __utmz=30149280.1515935454.62.19.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); dbcl2="1319642:3oodiNRPLsA"; ck=bhx0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1516369227%2C%22https%3A%2F%2Fmovie.douban.com%2Fsubject%2F26920017%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1276413593.1495944664.1516362206.1516369229.69; __utmt=1; _pk_id.100001.8cb4=92407ee5e36200eb.1495944661.54.1516369392.1516365282.; __utmb=30149280.19.8.1516369268498'
header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Cookie":cookie,
    "Host":"www.douban.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

for i in range(1,3):
    url = url+str(i)
    urlwb = requests.get(url,headers=header).text
    soup = BeautifulSoup(urlwb,"html5lib")
    people = soup.select("div.text")
    say = soup.select("div.content > div.title")

    for p,s in zip(people,say):
        p= p.get_text()
        hre = s.a.get("href")
        title = s.get_text()
        yy = {p.strip()+title.strip():hre}
        print (yy)

