from django.contrib import admin
from .models import Department, Position, Area, Employee 
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')
    list_display_links = ('id', 'city')

@admin.register(Employee)
class EmpoyeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'sex', 'birthday', 'phone', 'status', 'entry')
    list_display_links = ('id', 'name')