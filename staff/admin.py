from django.contrib import admin
from staff.models import Teacher

from unfold.admin import ModelAdmin

@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ("last_name", "initials", "account")
    search_fields = ("last_name",)

    def initials(self, obj):
        return f"{obj.first_name[0]}. {obj.middle_name[0] + '.' if obj.middle_name else ''}"
    
    initials.short_description = "Инициалы"