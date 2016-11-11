# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
        def new(self):
                pass

        def popular(self):
                pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255,null = True)
    text = models.TextField(null = True)
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(null = True)
    author = models.ForeignKey(User, related_name="asked_questions", null = True)
    likes = models.ManyToManyField(User, related_name="liked_questions",null = True)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)



'''
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа
'''