# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Posts(models.Model):
    post_id     = models.AutoField(primary_key=True)
    username    = models.CharField(max_length=60, blank=True)
    parent_id   = models.IntegerField(blank=True, null=True)
    post_text   = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField()
    thread_id   = models.IntegerField()
    deleted     = models.IntegerField(blank=True, null=True)
    class Meta:
        app_label='forum'
        managed = True
        db_table = 'posts'

class Threads(models.Model):
    thread_id     = models.AutoField(primary_key=True)
    thread_title  = models.CharField(max_length=60)
    first_post_id = models.IntegerField(null=True)
    date_posted   = models.DateTimeField(blank=True, null=True)
    username      = models.CharField(max_length=60, blank=True)
    class Meta:
        app_label='forum'
        managed = True
        db_table = 'threads'

