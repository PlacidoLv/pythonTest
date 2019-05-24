# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonTest.settings")
django.setup()


from wordcloud import WordCloud, ImageColorGenerator


from Huxiu.models import news as NewsModel


def getNewsContent():

   news = NewsModel.objects.all()

   content = ""

   for new in news:
       content = "%s，%s" % (content, new.content)

   return content

def createWordCloud():

    text = getNewsContent()

    width = 1000
    height = 1000

    wc = WordCloud(font_path="../simhei.ttf",
                   width=width,
                   height=height)

    wc.generate(text)
    wc.to_file("wordcloud1.jpg")

createWordCloud()