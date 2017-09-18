# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import urllib2
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getPrice(Kurl):
        content = requests.get(
            url = Kurl
            #url= 'https://www.ptt.cc/bbs/' + board + '/index.html',
            #cookies={'over18': '1'}
        ).content.decode('utf-8')
        try:
                price = content.split("[交易價格]：")[1].split("\n")[0]
                price = price.replace(",","")
                price = price.replace("，","")
                return int(re.search(r'\d+', price).group())
                #return price
        except:
                return -1

f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:
        break
    tmp = line.split("\t")
    price = getPrice(tmp[0])
    if price < 30000:
        print line+str(price)+"\n"
#print getPrice("https://www.ptt.cc/bbs/MacShop/M.1505715031.A.654.html")
