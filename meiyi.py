#!/usr/bin/python3

import requests
import bs4
import datetime
import glob
import io
import os
import sys

doc =  bs4.BeautifulSoup(requests.get("http://meiyizone.lofter.com").content)
sides = doc.find_all(attrs="side")
now = datetime.datetime.now()
current_day = "%.2d" % now.day
current_month = "%.2d" % now.month
current_year = "%.4d" %now.year

current_month = "03"
current_day = "21"


prefix = "/home/ren/play/meiyizone.github.io/_posts/%s-%s-%s-ornament" % (current_year, current_month, current_day)

def process_url(url):
    document = bs4.BeautifulSoup(requests.get(url).content)
    imgs = document.find_all(attrs="imgclasstag")
    return [img.get("bigimgsrc") for img in imgs]



img_list = []

for side in sides:
    months = side.find_all(attrs="month")
    days = side.find_all(attrs="day")
    assert len(months) == 1 and len(days) == 1
    month = months[0].text
    day = days[0].text
    print("{}-{}".format(month, day))
    if day == current_day and month == current_month:
        url = days[0].find("a").get("href")
        img_list += process_url(url)

if len(img_list) == 0:
    sys.exit(-1)

print(img_list)

#rm all the existing post of today

for filename in glob.glob("%s*" % prefix):
    os.remove(filename)

count = 1
for img in img_list:
    handle = io.open("%s-%d.markdown" % (prefix, count), "w")
    handle.writelines(["---\n",
        "layout: post\n",
        "title: 美艺空间手工饰品 %s-%s-%s-%d\n" % (current_year, current_month, current_day, count),
        "description: 美艺空间手工饰品\n",
        "date: %s-%s-%s\n" % (current_year, current_month, current_day),
        "img: %s\n" % img,
        "author: Xiaomeng\n",
        "---"])
    handle.close()
    count = count + 1


