from rest_framework import serializers

from students.models import Course, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

class StunentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id',"name")