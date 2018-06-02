from django.contrib import admin
from .models import Bookmark
# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Bookmark,BookmarkAdmin)




# id : root
# passwd : 정보통신 (wjdqhxhdtls)