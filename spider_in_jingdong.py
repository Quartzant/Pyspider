# -*- coding:utf-8 -*- 
__auther__ = 'Zins'
__date__ = '2017/12/2 15:11'

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getHTMLTEXT(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(goods_data, html):
    soup = BeautifulSoup(html, "html.parser")
    lis = soup.find_all('li', class_="gl-item")
    # print(len(lis))
    for i in range(len(lis)):
        try:
            # 获取商品信息 div 中的第一个 a 标签， 获取 title 属性值
            title = lis[i].a['title']
            # print(title)
            # 获取商品的价格信息
            price = lis[i].find('div', class_='p-price').i.string
            # print(price)
            goods_data.append([price, title])
        except:
            print('')

def printInfo(ilt):
    tplt = "{:8}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = "小米"
    depth = 1
    start_urls = 'https://search.jd.com/Search?keyword=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_urls + goods +  "&enc=utf-8&wq=" + goods   + '&page=' + str(57*i)
           #url = url_basic + keyword + '&enc=utf-8&wq=' + keyword + '&page=' + str(page)
            html = getHTMLTEXT(url)
            parsePage(infoList, html)
        except:
            continue
    printInfo(infoList)

main()