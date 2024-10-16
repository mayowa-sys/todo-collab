from django.db import models

class todoModel(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.CharField(max_length = 200)
    