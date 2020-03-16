from django.contrib import admin
from .models import BoardModel, BoardImage

# Register your models here.

class BoardModelAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('pk', 'title', 'author', 'created_at', 'updated_at')
    # 一覧表示画面のソート
    ordering = ('created_at',)  # '-created_at' とすると降順になります。
    # 編集画面のフィールド
    fields = ('title', 'author', 'content')

class BoardImageAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('pk', 'board')

admin.site.register(BoardImage, BoardImageAdmin)

admin.site.register(BoardModel, BoardModelAdmin)
