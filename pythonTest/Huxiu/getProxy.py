# -*- coding: UTF-8  -*-
# !/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from lxml import etree


def getKuaidailiIPList():

    listIP = []
    page = 1

    while page < 2:


        strurl = "http://www.kuaidaili.com/free/inha/%d" % page

        res = requests.get(strurl, verify=False)
        res.encoding = 'utf-8'
        html = res.text


        headers = {'User-Agent':  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
        tree = etree.HTML(html, parser=None)
        trs = tree.xpath("//tbody/tr")

        for tr in trs:

            i = 0
            ipinfo = {}
            for tds in tr.xpath("td/text()"):

                text = tds.strip()
                text = text.replace("\n", "")

                if len(text) > 0:

                    if i == 0:
                        ipinfo["ip"] = text
                    if i == 1:
                        ipinfo["port"] = text

                    if i == 2:
                        if text != "高匿名":
                            ipinfo = {}

                    i = i + 1


            if len(ipinfo) == 2:
                iptext = "%s:%s" % (ipinfo["ip"], ipinfo["port"])
                listIP.append(ipinfo)
        page = page + 1

    print listIP
    return listIP

getKuaidailiIPList()