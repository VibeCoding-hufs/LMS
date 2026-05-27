from rest_framework import serializers
from .models import Courses


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'credits']
