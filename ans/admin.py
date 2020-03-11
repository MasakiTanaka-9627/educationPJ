from django.contrib import admin
from .models import AnsModel

# Register your models here.

class AnsModelAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('board_id', 'author', 'created_at')
    # 一覧表示画面のソート
    ordering = ('created_at',)  # '-created_at' とすると降順になります。
    # 編集画面のフィールド
    fields = ('author', 'content', 'board_id')

admin.site.register(AnsModel, AnsModelAdmin)