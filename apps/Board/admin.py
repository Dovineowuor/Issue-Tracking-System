from django.contrib import admin

# Register your models here.
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name']