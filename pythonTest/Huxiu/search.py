# -*- coding: UTF-8  -*-
# !/usr/bin/python

from getHtml import getHtml as GetHtml
import json
import time
import datetime


from lxml import etree
import hashlib

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonTest.settings")
django.setup()

from Huxiu.models import news as NewsModel


getHtml = GetHtml()


def test():

    f = open('./test.html', 'r')
    text = f.read()

    tree = etree.HTML(text)
    print tree.xpath("/html/body/div")
    # alla = tree.xpath("/html/body/div/a")
    # for  item in  alla:
    #     print item.xpath("@href")
    #     print item.xpath("text()")
    #
    # for a in alla:
    #     print a.xpath("@href")
    #     print a.xpath("@class")
    #     print a.xpath("text()")
    # print tree.xpath("//a/@href")
    # divs = tree.xpath("/html/body/div")
    #
    # print len(divs)
    #
    # for item in divs:
    #
    #
    #     print item.xpath("text()")

# test()

def getContent(last_dateline):

    param = {"last_dateline": last_dateline}

    jsonStr = getHtml.getHtmlSource("https://www.huxiu.com/moment/ajaxGetList", param)
    jsonDic = json.loads(jsonStr)

    if jsonDic["success"] == True:

        html = jsonDic["data"]["data"]

        #构造了一个XPath解析对象
        tree = etree.HTML(html)


        liTree = tree.xpath("//li[@data-mid]")
        
        # print html
        # print "%d" % len(liTree)
        idx = 0


        for liItem in liTree:

            contentTree = liItem.xpath("./div[@class='mt-module-list-con']/div[@class='mt-list-cont mt-list-con-ellipsis']/p[@class='mt-list-cont-con']")

            authorTree = liItem.xpath(
                "./div[@class='mt-author-intro-wrap flex-mt-author-top-intro']/div[@class='mt-author-top-intro']/span/a/text()")

            author = authorTree[0]
            id = liItem.xpath("@data-mid")[0]


            content = ""

            for item in contentTree:

                for con in item.xpath("text()"):

                    content = "%s%s" % (content, con.replace("\n", "").strip())
            print id
            print "%d\n作者：%s\n内容：%s" % (idx, author, content)



            try:
                news = NewsModel()
                news.id = id
                news.author = author
                news.content = content
                news.time = last_dateline
                news.save()

            except Exception as e:

                print "保存失败"
            idx = idx + 1

    else:
        print "错误"


    return jsonDic["data"]["last_dateline"]



def getContentList():

    dateline = "%.0f" % time.time()

    today = datetime.date.today()

    # 昨天结束时间戳
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1

    # 今天开始时间戳
    today_start_time = yesterday_end_time + 1

    print today_start_time
    dateline = getContent(dateline)
    # while int(dateline) >= int(today_start_time):
    #
    #     dateline = getContent(dateline)
    #     print "dateline：%s" % dateline
    # print "爬取完毕"
# getContentList()


print getHtml.getHtmlSource("http://httpbin.org/get", None)
# print getHtml.getHtmlSource("http://www.baidu11.com", None)