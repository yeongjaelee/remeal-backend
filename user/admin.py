from django.contrib import admin

from user.models import User, UserContent


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

@admin.register(UserContent)
class UserContentAdmin(admin.ModelAdmin):
    pass