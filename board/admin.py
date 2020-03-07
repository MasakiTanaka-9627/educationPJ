from django.contrib import admin
from .models import BoardModel

# Register your models here.

class BoardModelAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('title', 'author', 'created_at', 'updated_at')
    # 一覧表示画面のソート
    ordering = ('created_at',)  # '-created_at' とすると降順になります。
    # 編集画面のフィールド
    fields = ('title', 'author', 'content')

admin.site.register(BoardModel, BoardModelAdmin)
