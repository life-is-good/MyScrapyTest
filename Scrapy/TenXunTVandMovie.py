# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import codecs
import urllib2
from bs4 import BeautifulSoup 

class Tenxun(object):
    url=["http://v.qq.com/rank/detail/1_-1_-1_-1_3_-1.html","http://v.qq.com/rank/detail/2_-1_-1_-1_2_-1.html"]
   
    def get_data(self,browser=None):
        if browser is None:
            new_browser = webdriver.Firefox()
        else:
            new_browser=browser
        result1=[]
        result2=[]
        for x in range(2):
            new_browser.get(self.url[x])
            time.sleep(1)
            new_browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[2]").click()
            time.sleep(1)
            i=1
            temp=[]
            while(i<=50):
                one=new_browser.find_element_by_xpath("//*[@id=\"mod_list\"]/li[%d]"%(i))
                name=one.find_element_by_class_name("mod_rankbox_con_item_title").find_element_by_tag_name("a").get_attribute("title")
                count = one.find_element_by_class_name("mod_rankbox_con_list_click").find_element_by_tag_name("strong").text
                view = one.find_element_by_class_name("mod_rankbox_con_item_actor").text
                actorlist = ""
                alist = one.find_element_by_class_name("mod_rankbox_con_item_impor").find_elements_by_tag_name("a")
                for a in alist:
                    actorlist = actorlist + a.get_attribute("title")+"  "
                print actorlist
                nameurl = one.find_element_by_class_name("mod_rankbox_con_item_title").find_element_by_tag_name("a").get_attribute("href")
                tag,director = self.get_info(nameurl.split("/")[-1])
                temp.append([name,view,tag,director,actorlist,count])
                i+=1
            if x == 1:
                result1.append(temp)
            else:
                result2.append(temp)
        if browser is None:
            new_browser.close()
        return result1,result2
    
    def get_info(self,url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
        req = urllib2.Request("https://v.qq.com/x/cover/"+url)
        req.add_header('Referer','www.baidu.com')
        req.add_header('User-Agent',user_agent)
        html = urllib2.urlopen(req).read()
        bsobj = BeautifulSoup(html,'html.parser')
        tags = bsobj.find_all("a",{"_stat":"description:tag"})
        if tags:
            tag = ""
            for t in tags:
                tag = tag + " " + t.getText()
            print tag
        else:
            tag = ""
        director = bsobj.find("a",{"_stat":"desc:director"})
        if director:
            director = director.getText()
        else:
            director = ""
        return tag,director



my=Tenxun()
result1 = []
result1,result2 = my.get_data(webdriver.Chrome(executable_path = 'chromedriver'))

f = codecs.open("tenxun/tenxun_tv_lg.txt","w","utf8")
f.write("{"+'"content"'+':'+"[")
f.write("\r\n")
for temp in result1:
    for i in range(len(temp)):
        f.write('{'+'"name"'+':'+'"'+temp[i][0]+'"'+','+'"view"'+':'+'"'+temp[i][1]+'"'+','+'"tags"'+':'+'"'+temp[i][2]+'"'+','+'"director"'+':'+'"'+temp[i][3]+'"'+','+'"actor"'+':'+'"'+temp[i][4]+'"'+','+'"number"'+':'+'"'+temp[i][5]+'"'+'},')
        f.write("\r\n")

f.write("\r\n")
f.write("]}")
f.close()    

f = codecs.open("tenxun/tenxun_movie_lg.txt","w","utf8")
f.write("{"+'"content"'+':'+"[")
f.write("\r\n")
for temp in result2:
    for i in range(len(temp)):
        f.write('{'+'"name"'+':'+'"'+temp[i][0]+'"'+','+'"view"'+':'+'"'+temp[i][1]+'"'+','+'"tags"'+':'+'"'+temp[i][2]+'"'+','+'"director"'+':'+'"'+temp[i][3]+'"'+','+'"actor"'+':'+'"'+temp[i][4]+'"'+','+'"number"'+':'+'"'+temp[i][5]+'"'+'},')
        f.write("\r\n")
        
f.write("\r\n")
f.write("]}")
f.close()
    
    

