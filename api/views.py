from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *


# Create User instance
class CreateUser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class CourseCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CoursesView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseSearchView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        searh_query = self.request.query_params.get('search', None)
        if searh_query is not None:
            queryset = queryset.filter(name__icontains=searh_query)
        return queryset


class RetrieveCourse(generics.RetrieveAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UpdateCourse(generics.UpdateAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DestroyCourse(generics.DestroyAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

class StudentView(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
class StudentSearchAPIView(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

    # Perform search by query params
    # 127.0.0.1:8000/api/v2/3.2/students/search/?search=t
    def get_queryset(self):
        queryset = super().get_queryset()
        # Get the search query parameter from the request
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(std_name__icontains=search_query)
        return queryset

class RetrieveStudent(generics.RetrieveAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

class UpdateStudent(generics.UpdateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

class DestroyStudent(generics.DestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer