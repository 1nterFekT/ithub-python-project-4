from django.contrib import admin
from students.models import Student, Group

from unfold.admin import ModelAdmin

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = (
        "last_name",
        "initials",
        "group",
        "account"
    )

    search_fields = ("last_name",)
    list_filter = ("group",)

    def initials(self, obj):
        return f"{obj.first_name[0]}. {obj.middle_name[0] + '.' if obj.middle_name else ''}"
    
    initials.short_description = "Инициалы"

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ("title", "course")
    list_filter = ("course",)
    search_fields = ("title",)