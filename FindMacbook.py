# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import urllib2
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def getLastPage(board):
        content = requests.get(
            url= 'https://www.ptt.cc/bbs/' + board + '/index.html',
            #cookies={'over18': '1'}
        ).content.decode('utf-8')
        first_page = re.search(r'href="/bbs/' + board + '/index(\d+).html">&lsaquo;', content)
        if first_page is None:
            return 1
        #content = content.replace("\n","")
        return content,int(first_page.group(1)) + 1

def getPage(board,index):
        content = requests.get(
            url= 'https://www.ptt.cc/bbs/' + board + '/index'+str(index)+'.html',
            #cookies={'over18': '1'}
        ).content.decode('utf-8')
        #content = content.replace("\n","")
        return content

content0,pid = getLastPage("MacShop")
#content1 = getPage("mobilesales",pid-1)

for k in range(100):
    content = getPage("MacShop",pid-k)
    tmp = content.split("<div class=\"title\">")
    for i in range(1,len(tmp),1):
        try:
            tmpp = tmp[i].split("<a href=\"")[1].split("</a>")[0].split("\">")
            lower_name = tmpp[1].lower()
            #if ("iphone" in lower_name or "i phone" in lower_name) and "7" in lower_name and "s" in lower_name and "徵/" not in lower_name and "售出" not in lower_name and "換/" not in lower_name and "北" in lower_name:
            if ("macbook" in lower_name or "mac book" in lower_name) and "11" not in lower_name and "pro" not in lower_name and "[收購]" not in lower_name and "售出" not in lower_name and "換/" not in lower_name and "北" in lower_name:
                OO = tmp[i].split("<a href=\"")[1].split("</a>")[0].split("\">")
                print "https://www.ptt.cc"+OO[0]+"\t"+OO[1]
        except:
            pass
