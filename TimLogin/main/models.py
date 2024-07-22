from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author + "\n" + self.text
