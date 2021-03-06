from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    content = models.TextField()
    count_ans = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images', null=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.title