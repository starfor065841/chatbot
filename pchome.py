import json
import re
import requests
import os
import time
import urllib
from bs4 import BeautifulSoup as bs
#from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' #偽裝使用者
headers = {'User-Agent':user_agent,
          'server': 'PChome/1.0.4',
          'Referer': 'https://mall.pchome.com.tw/newarrival/'}



def search(target):
    pchome = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='
    img = 'https://b.ecimg.tw'
    s = target
    search = pchome + s
    print(search)
    res = requests.get(search)
    ress = res.text
    

    jd = json.loads(ress)
    items = []
    prices = []
    urls = []
    image_urls = []
    totalPage = jd['totalPage']
    currentPage = 1
    i = 0
    nextPage = search + '&page=' + str(currentPage) + '&sort=sale/dc'
    mainurl = 'http://24h.pchome.com.tw/prod/'

    res = requests.get(nextPage)
    ress = res.text
    

    jd = json.loads(ress)
    
    while currentPage <= totalPage:
        for item in jd['prods']:

            result = match(target, item['name'])
            if result >= 0.7:
                items.append(item['name'])
                prices.append(item['price'])
                image_url = img + item['picS']
                image_urls.append(image_url)
                url = mainurl + item['Id'] + ' '
                urls.append(url)
                print(item['name'])
            #print(prices[i])
            #print(urls[i])
            #print(image_urls[i])
            i += 1
        
        currentPage += 1
        nextPage = search + '&page=' + str(currentPage) + '&sort=sale/dc'
        print('!!!!!!!!!!!!!' + nextPage)
        if currentPage % 30 == 0:
            time.sleep(5)
        
        res = requests.get(nextPage)
        ress = res.text
        res_text_format = ress.replace('try{jsonpcb_newarrival(','').replace(');}catch(e){if(window.console){console.log(e);}}','')
        
        if(res_text_format[0] != '{'):
            break
    
        #print(ress)
        jd = json.loads(res_text_format)
       
        #jd = requests.get(nextPage).json()



    print()
    return items, prices, urls, image_urls


def firstPage(target):
    pchome = 'https://ecshweb.pchome.com.tw/search/v3.3/?q='
    s = urllib.parse.quote(target)
    search = pchome + s
    return search


def match(txt, item_name):
    aaa=[]
    a_count = 0
    b_count = 0

    for aa in txt:
        if aa in item_name:
            aaa.append('yes')
            a_count += 1
        else:
            aaa.append('no')
            b_count += 1
    result = (a_count / (a_count + b_count))
    print(result)
    
    return result
        