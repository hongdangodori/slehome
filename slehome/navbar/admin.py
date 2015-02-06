from django.contrib import admin
from navbar.models import Title, MenuList, MenuListForNonmembers

admin.site.register(Title)
admin.site.register(MenuList)
admin.site.register(MenuListForNonmembers)