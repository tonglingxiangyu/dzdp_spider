import requests
#import parsel
import csv
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time    #暂停程序，避免封号
import random
#from proxy import xdaili_proxy, general_proxy
import re

#设置url、文件路径和cookie
url='https://www.dianping.com/shop/G8pp74mGZtksud47/review_all'
file = '人民公园1.csv'
cookie='_lxsdk_cuid=187993d2a59c8-08c88fc6fcba7-26031b51-280000-187993d2a59c8; _lxsdk=187993d2a59c8-08c88fc6fcba7-26031b51-280000-187993d2a59c8; WEBDFPID=1681903135511QKOGQUCfd79fef3d01d5e9aadc18ccd4d0c95072357-1681903135511-1681903135511QKOGQUCfd79fef3d01d5e9aadc18ccd4d0c95072357; _hc.v=82976948-a5c8-ec63-1c39-206548bd668f.1681903137; fspop=test; cy=427; cye=jiangyin; dper=3ed3f7dc085c04db172e2a2856222c094f930dc7b3af3a96f6744a3d032a7fdb49268dd20f42ad9840b5e0af0e702794e5a0860fa1e245fc15c33de049c9073e; qruuid=bea88d8e-7158-4784-a1e4-2d3350f111bc; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1681903192; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1681903593; _lxsdk_s=187993d2a5a-ec0-53c-f8e%7C%7C86'

#proxies = xdaili_proxy()

f = open(file, mode='w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(["用户名", "评论", "日期"])
#f_html= open('1.txt', mode='r', encoding='utf-8', newline='')
# csv_writer = csv.DictWriter(f, fieldnames=[
#     '用户名',
#     '评论时间',
#     '评论',
# ])
# csv_writer.writeheader()

headers = {"Cookie": cookie,
           'X-Requested-With': 'XMLHttpRequest',
            'host': 'www.dianping.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': UserAgent().random
            }

start = 0
for i in range(start,525):
    urls = url + '/p' + str(i)
    #response = requests.get(url=urls, headers=headers, proxies=proxies)
    response = requests.get(url=urls, headers=headers)
    #print(response.text)
    f_html = response.text
    soup = BeautifulSoup(f_html, 'html.parser')

    reviews = []
    # names=[]
    # review_content=[]
    # dates=[]

    #for soup1 in soup.find_all('div', class_='reviews-items'):
    for review_item in soup.find_all('li'):
        content = review_item.find('div', class_='review-words')
        if content:
            pass
        else:
            content = review_item.find('div', class_='review-words')
        if content != None:
            content = content.text.strip()[:-4].strip()
            content = content.replace('\n','')
        else :
            continue

        user_name = review_item.find('a', class_='name')
        if user_name != None:
            user_name = user_name.text.strip()
            user_name = user_name.replace('\n', '')

        date1 = review_item.find('span', class_='time')
        if date1 != None:
            date1 = date1.text.strip()
            date1 = date1.split(' ')[0]
            date1 = date1.replace('\n', '')

        reviews.append({
            "user_name": user_name,
            "content": content,
            "date": date1,
        })

    # print(review_content)
    # print(names)
    # print(dates)
    print(reviews)
    f = open(file, mode='a', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for row in reviews:
        writer.writerow(row.values())
        #print(row.values())
    f.close()
    print('已爬取第' + str(i) + '页')
    time.sleep(60 + 10 * random.random())
# selector = parsel.Selector(response.text)
# title = selector.css('ul li .name::text').getall() #用户名
# count = selector.css('ul li .review-words::text').getall() #评论
# time = selector.css('ul li .time::text').getall() #日期
#
# for i in range(len(title)):
#     dit = {
#         '用户名': title[i],
#         '评论时间': time[i],
#         '评论': count[i],
#     }
#     csv_writer.writerow(dit)

