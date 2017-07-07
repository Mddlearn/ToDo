# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=50)
    flag = models.IntegerField(default=1)
    priority = models.IntegerField(default=0)
    pubtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.id, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']
