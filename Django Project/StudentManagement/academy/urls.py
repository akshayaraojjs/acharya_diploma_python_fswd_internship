from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_student, name='register_student'),
    path('add-course/', views.add_course, name='add_course'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    
    path('students/', views.student_list, name='student_list'),
    path('students/update/<int:pk>/', views.update_student, name='update_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/update/<int:pk>/', views.update_course, name='update_course'),
    path('courses/delete/<int:pk>/', views.delete_course, name='delete_course'),
]
