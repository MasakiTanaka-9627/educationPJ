from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, UserImage

class UserAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('id', 'username', 'email', 'last_login')

class ProfileModelAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('user', 'birth_day', 'location')

class AnsImageAdmin(admin.ModelAdmin):
    # 一覧表示画面のフィールド
    list_display = ('pk', 'user_id')

admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileModelAdmin)

admin.site.register(UserImage, AnsImageAdmin)