from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Sum

from courses.models import Course, Topic
from assignments.models import Submission, Assignment

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

    topics = course.discipline.topics.all().order_by("ordering_number")

    submissions = Submission.objects.filter(
        student=student,
        assignment__topic__discipline=course.discipline
    )

    submission_map = {
        s.assignment.topic_id: s for s in submissions
    }

    topics_data = []

    for topic in topics:
        assignment = getattr(topic, "assignment", None)
        submission = submission_map.get(topic.id)

        status = "not_submitted"

        if submission:
            if submission.score and submission.score > 0:
                status = "graded"
            else:
                status = "pending"
        
        topics_data.append({
            "topic": topic,
            "assignment": assignment,
            "submission": submission,
            "status": status
        })

    return render(request, "students/course_detail.html", {
        "course": course,
        "topics": topics_data
    })

@login_required(login_url="login")
@require_http_methods(["GET", "POST"])
def topic_detail(request, topic_id):
    student = get_student_or_none(request.user)

    if not student:
        return HttpResponseForbidden("Только студенты имеют доступ к этой странице")

    topic = get_object_or_404(
        Topic,
        id=topic_id
    )

    assignment = getattr(topic, "assignment", None)

    submission = None
    if assignment:
        submission = Submission.objects.filter(
            student=student,
            assignment=assignment
        ).first()

    if request.method == "POST" and assignment and not submission:
        answer = request.POST.get("answer")

        if answer:
            Submission.objects.create(
                student=student,
                assignment=assignment,
                answer=answer,
                score=0
            )

            messages.success(request, "Ответ отправлен на проверку")
            return redirect("topic_detail", topic_id=topic.id)

    return render(request, "students/topic_detail.html", {
        "topic": topic,
        "assignment": assignment,
        "submission": submission
    })