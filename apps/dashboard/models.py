# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=200)
    mess_wall = models.ForeignKey('login.user', related_name="wall_messages")
    mess_creator = models.ForeignKey('login.user', related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    comm_message = models.ForeignKey(Message, related_name="comments")
    comm_user = models.ForeignKey('login.user', related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

