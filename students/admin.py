from django.contrib import admin
from students.models import Student, Group

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "account", "group")
    search_fields = ("first_name", "last_name", "account__username")
    list_filter = ("group",)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    list_filter = ("course",)