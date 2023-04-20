import requests
#import parsel
import csv
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time    #暂停程序，避免封号
import random
#from proxy import xdaili_proxy, general_proxy
import re
<<<<<<< HEAD
import os

start = 1  # 开始爬取的页数

# 设置url、文件路径和cookie
url='https://www.dianping.com/shop/G8pp74mGZtksud47/review_all'
file = '1.csv'
cookie = '_lxsdk_cuid=187993d2a59c8-08c88fc6fcba7-26031b51-280000-187993d2a59c8; _lxsdk=187993d2a59c8-08c88fc6fcba7-26031b51-280000-187993d2a59c8; WEBDFPID=1681903135511QKOGQUCfd79fef3d01d5e9aadc18ccd4d0c95072357-1681903135511-1681903135511QKOGQUCfd79fef3d01d5e9aadc18ccd4d0c95072357; _hc.v=82976948-a5c8-ec63-1c39-206548bd668f.1681903137; fspop=test; cy=427; cye=jiangyin; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1681903192,1681976411; s_ViewType=10; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; dper=3ed3f7dc085c04db172e2a2856222c098b9951b56894057b520c7e0bb2372da36d00c30b6ce14ed1b533eb55f3b6de8b7b7305008c7875e17a41d6f7ff7f62ce; qruuid=454ae1e2-7193-4d68-bcf7-593c9a10527b; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1681992621; _lxsdk_s=1879e5aece8-449-0ca-f0c%7C%7C3099'


delay = 1  # 设置访问间隔

f = open(file, mode='a', encoding='utf-8', newline='')
if not os.path.exists(file):
    writer = csv.writer(f)
    writer.writerow(["用户名", "评论", "日期"])
=======

#设置url、文件路径和cookie
url='https://www.dianping.com/shop/G8pp74mGZtksud47/review_all'
file = '人民公园1.csv'
cookie='_lxsdk_cuid=187993d2a59c8-08c88fc6fcba7-26031b51-280000-187993d2a59c8; _lxsdk=187993d2a59c8-08c88fc6fcba7-26031b51-280000-187993d2a59c8; WEBDFPID=1681903135511QKOGQUCfd79fef3d01d5e9aadc18ccd4d0c95072357-1681903135511-1681903135511QKOGQUCfd79fef3d01d5e9aadc18ccd4d0c95072357; _hc.v=82976948-a5c8-ec63-1c39-206548bd668f.1681903137; fspop=test; cy=427; cye=jiangyin; dper=3ed3f7dc085c04db172e2a2856222c094f930dc7b3af3a96f6744a3d032a7fdb49268dd20f42ad9840b5e0af0e702794e5a0860fa1e245fc15c33de049c9073e; qruuid=bea88d8e-7158-4784-a1e4-2d3350f111bc; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1681903192; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1681903593; _lxsdk_s=187993d2a5a-ec0-53c-f8e%7C%7C86'

#proxies = xdaili_proxy()

f = open(file, mode='w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(["用户名", "评论", "日期"])
>>>>>>> f432f666d904cc3cb63f2d8812f99f53f81fb0e3
#f_html= open('1.txt', mode='r', encoding='utf-8', newline='')
# csv_writer = csv.DictWriter(f, fieldnames=[
#     '用户名',
#     '评论时间',
#     '评论',
# ])
# csv_writer.writeheader()

<<<<<<< HEAD
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
=======
>>>>>>> f432f666d904cc3cb63f2d8812f99f53f81fb0e3
headers = {"Cookie": cookie,
           'X-Requested-With': 'XMLHttpRequest',
            'host': 'www.dianping.com',
            'Upgrade-Insecure-Requests': '1',
<<<<<<< HEAD
           'User-Agent': UA
            # 'User-Agent': UserAgent().random
            }


for i in range(start, 525):
    urls = url + '/p' + str(i)
    #response = requests.get(url=urls, headers=headers, proxies=proxies)
    response = requests.get(url=urls, headers=headers)
    print(response.status_code)
    if(response.status_code != 200):
        break
=======
            'User-Agent': UserAgent().random
            }

start = 0
for i in range(start,525):
    urls = url + '/p' + str(i)
    #response = requests.get(url=urls, headers=headers, proxies=proxies)
    response = requests.get(url=urls, headers=headers)
>>>>>>> f432f666d904cc3cb63f2d8812f99f53f81fb0e3
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
<<<<<<< HEAD
    time.sleep(delay + 5 * random.random())
=======
    time.sleep(60 + 10 * random.random())
>>>>>>> f432f666d904cc3cb63f2d8812f99f53f81fb0e3
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

