from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title