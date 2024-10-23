from django.db import models
from django.contrib.auth.models import User

#model for the basic functions of the todo app
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #To show the title of the todo when it is being accessed
    def __str__(self):
        return self.title