from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.views import Token

from .models import *


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', )

class StudentSerialzer(ModelSerializer):

    class Meta:
        model = Student
        fields = ('std_name', 'std_age', 'educational_year', 'courses')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
