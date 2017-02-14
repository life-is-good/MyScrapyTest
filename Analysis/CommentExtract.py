# -*- coding: utf-8 -*-
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import json
import os
import xlwt
import xlrd
path = os.getcwd()

def aiqiyi_jsontotxt(path):
    for filename in os.listdir(path):
        f = open(path+filename,"r")
        print filename
        data = json.load(f,encoding="utf-8")
        clist = []
        for comment in data["comment"]:
            for c in comment["content"]:
                clist.append(c)
        f.close()
        #写到excel
        table = xlwt.Workbook()
        sheet = table.add_sheet('comment')
        for i in range(len(clist)):
            sheet.write(i, 0 , clist[i])
        table.save(path+data["name"]+'.xls')
        #写到txt
#         fw = open(path+data["name"]+".txt","w")
#         for c in clist:
#             fw.write(c)
#             fw.write("\n")
#         fw.close()

#按照日期将评论存放起来
def classifydate(filename):
    table = xlrd.open_workbook(filename)
    table = table.sheet_by_index(0)

    moviedict = {}
    data_value = table.col_values(4)
    comment = table.col_values(5)
    for i in range(len(data_value)):
        moviedict.setdefault(data_value[i],[]).append(comment[i])
    #按照日期进行排序
    moviedict_sorted = sorted(moviedict.items(), key=lambda moviedict:sort_date(moviedict[0]))
    #存到txt，只存日期和数量    
    f = open("classifierdata/commentnumber.txt","w")
    f.write("{"+'"content"'+':'+"[")
    f.write("\n")
    for (k,v) in moviedict_sorted:
        print k
        #按照时间将评论分开
        e = xlwt.Workbook()
        sheet1 = e.add_sheet(u'Sheet1')
        for i in range(len(v)):
            sheet1.write(i,0,v[i])     
        e.save("classifierdata/"+k+'.xls')
        f.write('{'+'"date"'+':'+'"'+k+'"'+","+'"number"'+":"+'"'+str(len(v))+'"'+"}"+","+"\n")
    f.write("\n")
    f.write("]}")
    f.close()
    return moviedict

#将时间转换成int
def sort_date(date):
    d = date.split("-")
    s = ""
    for i in d:
        s = s + i
    return int(s)

#提取关键词和关键短语和摘要
def extract_keyword():
    text = codecs.open('greatwall.txt', 'r', 'utf-8').read()
    tr4w = TextRank4Keyword(stop_words_file = 'stopword.txt')  # 导入停止词
    #使用词性过滤，文本小写，窗口为2
    tr4w.analyze(text=text, lower=True, window=2)

    print '关键词：'
    for item in tr4w.get_keywords(20, word_min_len=2):
        print item.word
        print item.weight
    
    print '关键短语：'
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
        print phrase
    
    tr4s = TextRank4Sentence(stop_words_file = 'stopword.txt')
    tr4s.analyze(text=text, lower=True, source = 'all_filters')

    print '摘要：'
    for item in tr4s.get_key_sentences(num=3):
        print(item.index, item.weight, item.sentence)

def keyword_tojson():
    fr = open("keywords.txt","r")
    result = []
    for line in fr.readlines():
        json = line.split("，")
        result.append(json)
    fr.close()
    f = open("keywords.txt","w")
    f.write("{"+'"content"'+':'+"[")
    f.write("\n")
    for r in result:
        f.write('{'+'"keyword"'+':'+'"'+r[0]+'"'+","+'"number"'+":"+'"'+r[1].strip("\n")+'"'+"}"+","+"\n")
    f.write("]}")
    f.close()

if __name__ == "__main__":
#     keyword_tojson()
#     extract_keyword()
#       classifydate(path+"\\test.xls")
#     path = os.getcwd()+"/aiqiyi_tv/"
    aiqiyi_jsontotxt(path)





        
    
