from rest_framework import serializers

from courses.models import Courses

class CourseListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='Courses.name')
    credits = serializers.IntegerField(source='Courses.credits')

    class Meta:
        model = Courses
        fields = ["id", "name", "credits"]


class CourseDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='Courses.name')
    from notices.serializers import NoticeListSerializer
    notices = NoticeListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Courses
        fields = ["id", "name", "credits"]