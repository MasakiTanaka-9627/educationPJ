from django.db import models
from django.utils import timezone
from board.models import BoardModel

# Create your models here.

class AnsModel(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=50)
    board_id = models.ForeignKey(BoardModel, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.author