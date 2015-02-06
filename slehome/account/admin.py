from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from account.models import MyUser, BasicMemberInformation
from account.models import AccountSettingsMenuList
from account.models import MemberIntro, PhotoLink, Stat



# Account 메뉴의 서브메뉴
admin.site.register(AccountSettingsMenuList)



# MyUser를 User의 Admin Page에서 관리할 수 있게 함
class MyUserInline(admin.StackedInline):
	model = MyUser

class UserAdmin(UserAdmin):
	inlines = (MyUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)



# 슬기짜기 멤버의 기본 데이터
admin.site.register(BasicMemberInformation)



# PhotoLink, Statdmf MemberIntro의 Admin Page에서 관리할 수 있게 함
class PhotoLinkInline(admin.StackedInline):
	model = PhotoLink

class StatInline(admin.StackedInline):
	model = Stat

class MemberIntroAdmin(admin.ModelAdmin):
	list_display = ('user', 'intro',)
	inlines = (PhotoLinkInline, StatInline, )

admin.site.register(MemberIntro, MemberIntroAdmin)