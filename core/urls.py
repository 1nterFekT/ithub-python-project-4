from django.contrib import admin
from django.urls import path
from accounts import views as auth_views
from students import views as student_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("auth/login/", auth_views.login_view, name="login"),
    path("auth/logout/", auth_views.logout_view, name="logout"),

    path("courses/", student_views.courses_list, name="courses"),
    path("courses/<int:course_id>/", student_views.course_detail, name="course_detail"),

    path("topics/<int:topic_id>/", student_views.topic_detail, name="topic_detail"),
]
