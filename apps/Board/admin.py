from django.contrib import admin
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_description', 'created_at', 'updated_at', 'project']

    def get_description(self, obj):
        return obj.description_field_name
    get_description.short_description = 'Description'

# This requires object or render the attributes as properties of the board admin see
# above the object oriented solution
# from django.contrib import admin
# from .models import Board

# @admin.register(Board)
# class BoardAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'created_at', 'updated_at', 'project']
# from django.contrib import admin

# # Register your models here.
# from .models import Board

# @admin.register(Board)
# class BoardAdmin(admin.ModelAdmin):
#     list_display = ['name']
