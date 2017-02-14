# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
from time import sleep
from bs4 import BeautifulSoup 
from selenium import webdriver
import re
import random
import time
from PIL import Image
import shutil

useragent= ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0']
            
def star():
    i=0
    fstar = open('star.txt','w')
    while (i<=18480):
        print i
        try:
            req = urllib2.Request('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.ph'
                                  'p?resource_id=28226&from_mid=1&&format=j'
                                  'son&ie=utf-8&oe=utf-8&query=%E6%98%8E%E6%98%9F&'
                                  'sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=' + str(i) + '&rn=12')
            req.add_header('Referer', 'www.baidu.com')
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')
            html = urllib2.urlopen(req).read()
            datadic = json.loads(html)['data'][0]['result']
    
            for data in datadic:
                print>> fstar, data['ename'].encode('utf8')
                print data['ename'].encode('UTF8')
            i = i+12
        except:
            sleep(0)
            continue
    fstar.close()
    print "star done"
    
def movie():
    i=0
    fmovie = open('movie.txt','w')
    while(i<760):
        print i
        try:
            req = urllib2.Request('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6862&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E7%94%B5%E5%BD%B1&sort_key=16&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn='+str(i)+'&rn=8')
            req.add_header('Referer','www.baidu.com')
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')
            html = urllib2.urlopen(req).read()
            datadic = json.loads(html)['data'][0]['disp_data']
            print "======================"
            for data in datadic:
                print>> fmovie,data['ename'].encode('utf8')
                print data['ename'].encode('UTF8')
            i += 8
        except:
            sleep(0)
            continue
    fmovie.close()
    print "movie done"

def time_star_name():
    f = open('ip.txt')
    lines = f.readlines()
    proxies = []
    for line in range(0, len(lines)):
        proxy = lines[line].strip('\n')
        proxies.append(proxy)
    proxy = {'http': 'http://125.82.105.141:808'}    
    
    namelist = [] 
    f = open("time_name.txt","w")
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    i = 1
    while (i<50):    
        try:
            print i
            req = urllib2.Request('http://service.channel.mtime.com/service/search.mcs?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Pages.SearchService&Ajax_CallBackMethod=SearchPersonByCategory&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2Fpeople%2Fsearch%2Fsection%2F%23constellation%3D0%26bloodType%3D100%26pageIndex%3D2%26filmographyId%3D1&Ajax_CallBackArgument0=&Ajax_CallBackArgument1=0&Ajax_CallBackArgument2=0&Ajax_CallBackArgument3=100&Ajax_CallBackArgument4=1&Ajax_CallBackArgument5=0&Ajax_CallBackArgument6=0&Ajax_CallBackArgument7=0&Ajax_CallBackArgument8=0&Ajax_CallBackArgument9=0&Ajax_CallBackArgument10=0&Ajax_CallBackArgument11=4&Ajax_CallBackArgument12='+str(i)+'&Ajax_CallBackArgument13=0')
            req.add_header('Referer','www.baidu.com')
            req.add_header('User-Agent',user_agent)
            opener = urllib2.build_opener(urllib2.ProxyHandler(proxy))                
            #html = urllib2.urlopen(req).read()
            html = opener.open(req).read()
    
            pattern=re.compile(r'title=\\"(.*?)/',re.S)
            alist = pattern.findall(html)
            namelist.extend(alist)
            i += 1
            for name in alist:
                print name
            sleep(random.uniform(1,2.5))
        except:
            user_agent = random.choice(useragent)
            print user_agent
        
    for name in namelist:
        if name:
            f.write(name)
            f.write('\r\n')
    f.close()
 
   
def star_1905_name():
    f = open("starname1905.txt","w+")
    namelist = []     
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    word = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for w in word:
        print w
        req = urllib2.Request("http://www.1905.com/list.php?catid=204&a=0&l="+w)
        req.add_header('Referer','www.baidu.com')
        req.add_header('User-Agent',user_agent)
        html = urllib2.urlopen(req).read()
        bsobj = BeautifulSoup(html,'html.parser')
        llist = bsobj.find_all("li", {"class":"star_usercen"})
        for l in llist:
            print l.find("a").getText()
            namelist.append(l.find("a").getText())
    for name in namelist:
        if(name):
            f.write(name)
            f.write("\n")
    f.close()

def moive_1905_name():
    f = open("moviename1905.txt","a")
    namelist = []     
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    i = 1
    while i<505:
        print i
        req = urllib2.Request("http://www.1905.com/mdb/film/list/clime-1/o0d0p"+str(i)+".html")
        req.add_header('Referer','www.baidu.com')
        req.add_header('User-Agent',user_agent)
        html = urllib2.urlopen(req).read()
        bsobj = BeautifulSoup(html,'html.parser')
        divlist = bsobj.find_all("div", {"class":"text"})
        for l in divlist:
            print l.find("a").getText()     
            namelist.append(l.find("a").getText())
        i += 1    
    for name in namelist:
        if(name and len(name) < 10):
            f.write(name)
            f.write("\n")
    f.close()

def baidu_board():
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    url = ["http://top.baidu.com/buzz?b=26&c=1&fr=topcategory_c1",
           "http://top.baidu.com/buzz?b=4&c=2&fr=topcategory_c2",
           "http://top.baidu.com/buzz?b=19&c=3&fr=topcategory_c3"]
    result = {}
    for j in range(len(url)):
        req = urllib2.Request(url[j])
        req.add_header('Referer','www.baidu.com')
        req.add_header('User-Agent',user_agent)
        html = urllib2.urlopen(req).read()
        bsobj = BeautifulSoup(html,'html.parser')
        namelist = bsobj.find_all("td", {"class":"keyword"})
        indexlist = bsobj.find_all("td", {"class":"last"})
        infourllist = bsobj.find_all("td", {"class":"tc"})
    
        if j==0:
            for i in range(50):
                print namelist[i].find("a").getText()
                inforesult = []
                inforesult = baidu_board_info(infourllist[i].find("a").get("href"))
                result.setdefault("movie",[]).append((namelist[i].find("a").getText(),inforesult,indexlist[i].find("span").getText()))
        elif j==1:
            for i in range(50):
                print namelist[i].find("a").getText()
                inforesult = []
                inforesult = baidu_board_info(infourllist[i].find("a").get("href"))
                result.setdefault("tv",[]).append((namelist[i].find("a").getText(),inforesult,indexlist[i].find("span").getText()))
        else:
            for i in range(50):
                print namelist[i].find("a").getText()
                inforesult = []
                inforesult = baidu_board_info(infourllist[i].find("a").get("href"))
                result.setdefault("show",[]).append((namelist[i].find("a").getText(),inforesult,indexlist[i].find("span").getText()))
                
    f = open("baidu_all","w")
    for k,v in result.items():
        print k
        for value in v:
            f.write(value[0]+"|")
            for i in value[1]:
                f.write(i[0]+":"+i[1]+"|")
            f.write(value[2])
            f.write("\n")
    f.close()            
    return result

def baidu_board_info(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    req = urllib2.Request(url)
    req.add_header('Referer','www.baidu.com')
    req.add_header('User-Agent',user_agent)
    html = urllib2.urlopen(req).read()
    bsobj = BeautifulSoup(html,'html.parser')
    dtlist = bsobj.find_all("dt",{"class":"basicInfo-item name"})
    ddlist = bsobj.find_all("dd",{"class":"basicInfo-item value"})
    inforesult = []
    for i in range(len(dtlist)):
        inforesult.append((dtlist[i].getText(),ddlist[i].getText()))
    return inforesult


# def douban_info():
#     
#     urllist =["https://movie.douban.com/subject/6982558/","https://movie.douban.com/subject/26325320/",
#           "https://movie.douban.com/subject/26683290/","https://movie.douban.com/subject/25815034/",
#           "https://movie.douban.com/subject/26836588/","https://movie.douban.com/subject/24751763/",
#           "https://movie.douban.com/subject/25921812/","https://movie.douban.com/subject/25884877/",
#           "https://movie.douban.com/subject/26280528/","https://movie.douban.com/subject/25911694/"]
#     user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
#     
#     for i in range(len(urllist)):
#         namelist = []
#         infolist = []
#         req = urllib2.Request(urllist[i])
#         req.add_header('Referer','www.baidu.com')
#         req.add_header('User-Agent',user_agent)
#         html = urllib2.urlopen(req).read()  
#         bsobj = BeautifulSoup(html,'html.parser')
#         #海报图
#         pic = bsobj.find("img",{"rel":"v:image"}).get("src")
#         urllib.urlretrieve(pic,"douban/movie"+'%s.jpg' % (i+1))
#         #电影名
#         name = bsobj.find("span",{"property":"v:itemreviewed"}).getText()
#         namelist.append("电影名称")
#         infolist.append(name)
#         #电影信息
#         div = bsobj.find("div",{"id":"info"})
#         for line in div.getText().split("\n"):
#             if line:
#                 print line.split(":")[-1]
#                 namelist.append(line.split(":")[0])
#                 infolist.append(line.split(":")[-1])
#         #简介 
#         brief = bsobj.find("span",{"property":"v:summary"})
#         namelist.append("简介")
#         infolist.append(brief.getText().strip())
#         #存成json形式
#         f = open("douban/"+name+".txt","w")
#         f.write("{"+'"content"'+':'+"[")
#         f.write("\n")
#         for i in range(len(infolist)):
#             f.write('{'+'"name"'+':'+'"'+namelist[i]+'"'+","+'"value"'+":"+'"'+infolist[i]+'"'+"}"+",")
#             f.write("\n")
#         f.write("\n")
#         f.write("]}")
#         f.close() 

#  按照宽度进行所需比例缩放
def resize_by_width(cls, w_divide_h):
    im = Image.open(cls.infile)
    (x, y) = im.size
    x_s = x
    y_s = x/w_divide_h
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    out.save(cls.outfile)

def douban_info(id):
    
    url = "https://movie.douban.com/subject/"+id+"/"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    
    namelist = []
    infolist = []
    req = urllib2.Request(url)
    req.add_header('Referer','www.baidu.com')
    req.add_header('User-Agent',user_agent)
    html = urllib2.urlopen(req).read()  
    bsobj = BeautifulSoup(html,'html.parser')
    #电影名
    name = bsobj.find("span",{"property":"v:itemreviewed"}).getText()
    namelist.append("电影名称")
    infolist.append(name)
    #海报图
    pic = bsobj.find("img",{"rel":"v:image"}).get("src")
    urllib.urlretrieve(pic,"douban/"+'%s.jpg' % (name))
    #电影信息
    div = bsobj.find("div",{"id":"info"})
    for line in div.getText().split("\n"):
        if line:
            print line.split(":")[-1]
            namelist.append(line.split(":")[0])
            infolist.append(line.split(":")[-1])
    #简介 
    brief = bsobj.find("span",{"property":"v:summary"})
    namelist.append("简介")
    infolist.append(brief.getText().strip())
    #存成json形式
    f = open("douban/"+name+".txt","w")
    f.write("{"+'"content"'+':'+"[")
    f.write("\n")
    for i in range(len(infolist)):
        f.write('{'+'"name"'+':'+'"'+namelist[i]+'"'+","+'"value"'+":"+'"'+infolist[i]+'"'+"}"+",")
        f.write("\n")
    f.write("\n")
    f.write("]}")
    f.close()


def douban_movie_id(name):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'    
    req = urllib2.Request("https://movie.douban.com/subject_search?search_text="+name+"&cat=1002")
    req.add_header('Referer','www.baidu.com')
    req.add_header('User-Agent',user_agent)
    html = urllib2.urlopen(req).read()
    bsobj = BeautifulSoup(html,'html.parser')
    div = bsobj.find("div",{"class":"pl2"})
    if div:
        return div.find("a").get("href").split("/")[-2]
    else:
        return None
    
def douban():
    namelist = ["长城","血战钢锯岭","你的名字","湄公河行动","生门",
                "罗曼蒂克消亡史","驴得水","爸爸的3次婚礼","从你的全世界路过","摆渡人"]
    for name in namelist:
        print name
        id = douban_movie_id(name)
        if id:
            douban_info(id)
        else:
            continue
        
if __name__ == "__main__":
    douban()  