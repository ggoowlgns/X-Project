from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bbs.model import Bbs

class BbsAdmin(admin.ModelAdmin):
    list_display=('title','author','created',)

admin.site.register(Bbs, BbsAdmin)