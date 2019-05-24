# -*- coding: UTF-8  -*-
# !/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from random import choice

import requests

import getProxy

import random

class getHtml:

    def __init__(self):

        self.proxyList = getProxy.getKuaidailiIPList()
        self.trytime = 0

        self.user_agent = [

            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        ]

    def getHtmlSource(self, strUrl, data):

        print "url：%s" % strUrl

        try:
            self.proxyList = getProxy.getKuaidailiIPList()
            user_agent = choice(self.user_agent)
            print user_agent
            headers = {'User-Agent': user_agent}
            print "self.proxyList - %s" % self.proxyList
            proxy = choice(self.proxyList)

            proxy_url = "http://%s:%s" % (proxy["ip"], proxy["port"])

            print proxy
            print proxy_url

            res = requests.post(strUrl, headers=headers, data=data, proxies={"http": proxy_url}, timeout=8) # verify=False,
            res.encoding = 'utf-8'

        except Exception as e:

            print "获取源码错误：%s" % e
            self.trytime = self.trytime + 1

            if self.trytime > 3:

                return None

            print "重试：%d次" % self.trytime
            return self.getHtmlSource(strUrl, data)

        return res.text
