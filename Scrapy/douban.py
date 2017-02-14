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