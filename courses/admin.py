from django.contrib import admin
from courses.models import Discipline, Course

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

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "discipline_title",
        "discipline_duration",
        "course_start",
        "course_end",
        "teacher",
        "group"
    )

    list_filter = (
        "teacher",
        "group",
        "course_start",
        "course_end"
    )

    search_fields = (
        "code",
        "discipline__title"
    )

    def discipline_title(self, obj):
        return obj.discipline.title
    
    def discipline_duration(self, obj):
        return obj.discipline.duration
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.groups.filter(name="teachers").exists():
            return qs.filter(teacher__acount=request.user)
        
        return qs