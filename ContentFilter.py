# -*- coding: UTF-8 -*-
# Kevin Yen-Kuan Lee
import urllib2
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def send_email(recipient, subject, body):
    import smtplib
    user = ""
    pwd = ""
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
        server_ssl.sendmail(FROM, TO, message)
        #server_ssl.quit()
        server_ssl.close()
        print 'successfully sent the mail'
    except Exception,e:
        print "failed to send mail"

def getPrice(Kurl):
        content = requests.get(
            url = Kurl
            #url= 'https://www.ptt.cc/bbs/' + board + '/index.html',
            #cookies={'over18': '1'}
        ).content.decode('utf-8')
        Time = "NO TIME"
        try:
            Time = content.split("時間</span><span class=\"article-meta-value\">")[1].split("<")[0]
        except:
            pass
        try:
                price = content.split("[交易價格]：")[1].split("\n")[0]
                price = price.replace(",","")
                price = price.replace("，","")
                return int(re.search(r'\d+', price).group()),Time
                #return price
        except:
                return -1,Time

UrlSet = set()
Mlist = list()
fr = open('output.txt','r')
while True:
    line = fr.readline()
    if not line:
        break
    line = line.replace("\n","")
    Mlist.append(line)
    try:
        UrlSet.add(line.split("\t")[1])
    except:
        pass
fr.close()

f = open(sys.argv[1],'r')
fw = open('output.txt','w')
while True:
    line = f.readline()
    if not line:
        break
    tmp = line.split("\t")
    price,Time = getPrice(tmp[0])
    if tmp[0] in UrlSet:
        continue
    if price < 30000:
        try:
            title = line.split("\t")[1].split("\n")[0]
            Iurl = line.split("\t")[0]
            send_email("yenkuanlee@gmail.com",title,Time+"\n\n"+title+"\n\n"+Iurl+"\n\n"+str(price)+" 元"+"\n\n")
            send_email("mnbm03409@gmail.com",title,Time+"\n\n"+title+"\n\n"+Iurl+"\n\n"+str(price)+" 元"+"\n\n")
        except:
            pass
        print Time+"\t"+line+str(price)+"\n"
        fw.write(Time+"\t"+line+str(price)+"\n\n")
f.close()

for x in Mlist:
    fw.write(x+"\n")
fw.close()

