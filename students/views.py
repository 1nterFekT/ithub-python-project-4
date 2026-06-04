from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Sum

from courses.models import Course
from assignments.models import Submission

def get_student_or_none(user):
    return getattr(user, "student", None)

@login_required(login_url="login")
def courses_list(request):
    student = get_student_or_none(request.user)

    if not student:
        return HttpResponseForbidden("Только студенты имеют доступ к этой странице")

    courses = Course.objects.filter(group=student.group)

    enriched_courses = []

    for course in courses:
        submissions = Submission.objects.filter(
            student=student,
            assignment__topic__discipline=course.discipline
        )

        total_score = submissions.aggregate(total=Sum("score"))["total"] or 0

        enriched_courses.append({
            "course": course,
            "score": total_score,
            "max_score": 100
        })

    return render(request, "students/courses_list.html", {
        "courses": enriched_courses
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