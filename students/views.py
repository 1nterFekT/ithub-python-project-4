from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from courses.models import Course

@login_required(login_url="login")
def courses_list(request):
    student = request.user.student
    courses = Course.objects.filter(group=student.group)

    return render(request, "students/courses_list.html", {
        "courses": courses
    })

@login_required(login_url="login")
def course_detail(request, course_id):
    student = request.user.student

    course = get_object_or_404(
        Course,
        id=course_id,
        group=student.group
    )

    return render(request, "students/course_detail.html", {
        "course": course
    })