# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')


class Question(models.Model):
	title = models.TextField()
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.TextField()
	likes = models.ManyToManyField(User)
	objects = QuestionManager()

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question)
	author = models.TextField()

