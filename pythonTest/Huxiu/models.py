# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.


class news(models.Model):

    id = models.CharField(u'id', primary_key=True, max_length = 32)

    author = models.CharField(u'来源id',  unique=False, max_length=100, default='', db_index=True)
    content = models.TextField(u'来源名字', default='')
    time = models.IntegerField(u"时间", default=0)

    list_display = ('name')
    #
    # def toJSON(self):
    #     import json
    #     dic = dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
    #     dic.pop("source_id")
    #     dic.pop("source_name")
    #     return json.dumps(dic)
    #
    # def toDic(self):
    #     return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
    #
    def __unicode__(self):
        return self.name

