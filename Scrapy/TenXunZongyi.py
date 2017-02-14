# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import codecs

class Tenxun(object):
    url = "http://v.qq.com/rank/detail/10_-1_-1_-1_2_-1.html"
    def get_data(self,browser=None):
        if browser is None:
            new_browser = webdriver.Firefox()
        else:
            new_browser=browser
        result=[]
        new_browser.get(self.url)
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
            temp.append([name,view,count])
            print name
            i+=1
        print(temp)
        result.append(temp)
        if browser is None:
            new_browser.close()
        return result

my=Tenxun()
result = []
result= my.get_data(webdriver.Chrome(executable_path = 'chromedriver'))

f = codecs.open("tenxun/tenxun_zongyi_lg.txt","w","utf8")
f.write("{"+'"content"'+':'+"[")
f.write("\r\n")
for temp in result:
    for i in range(len(temp)):
        f.write('{'+'"name"'+':'+'"'+temp[i][0]+'"'+','+'"view"'+':'+'"'+temp[i][1]+'"'+','+'"number"'+':'+'"'+temp[i][2]+'"'+'},')
        f.write("\r\n")
        
f.write("\r\n")
f.write("]}")
f.close()    

    
    


