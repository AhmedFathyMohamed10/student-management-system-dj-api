from django.urls import path
from .views import *


urlpatterns = [
    path('register/', CreateUser.as_view()),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('courses/search/', CourseSearchView.as_view(), name='courses-search'),
    path('create-course/', CourseCreate.as_view(), name='create-course'),
    path('courses/<str:pk>/', RetrieveCourse.as_view(), name='course'),
    path('courses/<str:pk>/update', UpdateCourse.as_view(), name='update-course'),
    path('courses/<str:pk>/delete', DestroyCourse.as_view(), name='delete-course'),
    #  All about students 
    path('create-student/', StudentCreate.as_view(), name='create-student'),
    path('students/', StudentView.as_view(), name='students'),
    path('students/search/', StudentSearchAPIView.as_view(), name='student-search'),
    path('students/<str:pk>/', RetrieveStudent.as_view(), name='students'),
    path('students/<str:pk>/update', UpdateStudent.as_view(), name='update-student'),
    path('students/<str:pk>/delete', DestroyStudent.as_view(), name='delete-student'),

]
