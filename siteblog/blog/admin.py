from django.contrib import admin
from .models import *


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')


admin.site.register(Useful_link, LinkAdmin)


class ContextAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')
    search_fields = ('title','content')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields =('title',)

admin.site.register(Context, ContextAdmin)
admin.site.register(Category, CategoryAdmin)