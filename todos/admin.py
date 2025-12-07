from django.contrib import admin
from .models import Todo
# Register your models here.

class AdminModels(admin.ModelAdmin):
    list_display=['task','is_completed','created_at','updated_at']

admin.site.register(Todo,AdminModels)