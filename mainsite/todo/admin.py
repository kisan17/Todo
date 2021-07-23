from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

class TodoListAdmin(admin.ModelAdmin):
    list_display=['title','content']


admin.site.register(Category,CategoryAdmin)
admin.site.register(TodoList,TodoListAdmin)
