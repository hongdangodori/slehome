from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from account.models import MyUser, BasicMemberInformation

class MyUserInline(admin.StackedInline):
	model = MyUser

class UserAdmin(UserAdmin):
	inlines = (MyUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(BasicMemberInformation)