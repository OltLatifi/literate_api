from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=300)
    approved = models.BooleanField(default=False)

class Joke(models.Model):
    text = models.CharField(max_length=500)
    approved = models.BooleanField(default=False)