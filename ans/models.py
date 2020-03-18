from django.db import models
from django.utils import timezone
from board.models import Board, User

# Create your models here.

class Ans(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.author