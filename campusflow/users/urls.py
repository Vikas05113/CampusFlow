from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('student-dashboard/', views.student_dashboard),
    path('teacher-dashboard/', views.teacher_dashboard),
    path('admin-dashboard/', views.admin_dashboard),
]