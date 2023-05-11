from django.contrib import admin

from user.models import User, UserContent, UserImage


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

@admin.register(UserContent)
class UserContentAdmin(admin.ModelAdmin):
    pass

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    pass