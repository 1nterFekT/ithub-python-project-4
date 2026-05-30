from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from courses.models import Course

def get_student_or_none(user):
    return getattr(user, "student", None)

@login_required(login_url="login")
def courses_list(request):
    student = get_student_or_none(request.user)

    if not student:
        return HttpResponseForbidden("Только студенты имеют доступ к этой странице")

    courses = Course.objects.filter(group=student.group)

    return render(request, "students/courses_list.html", {
        "courses": courses
    })

@login_required(login_url="login")
def course_detail(request, course_id):
    student = get_student_or_none(request.user)

    if not student:
        return HttpResponseForbidden("Только студенты имеют доступ к этой странице")

    course = get_object_or_404(
        Course,
        id=course_id,
        group=student.group
    )

    return render(request, "students/course_detail.html", {
        "course": course
    })