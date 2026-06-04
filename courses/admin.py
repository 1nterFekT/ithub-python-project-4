from django.contrib import admin
from courses.models import Discipline

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "duration",
        "curriculum",
        "updated_at"
    )

    list_filter = ("title", "duration")
    search_fields = ("title",)