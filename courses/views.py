from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Courses, Enrollment
from .serializers import CourseListSerializer


class CourseListView(APIView):
    def get(self, request, userId):
        courses = Courses.objects.filter(enrollments__user_id=userId)
        if not courses.exists():
            raise NotFound('수강 중인 과목이 없습니다.')
        serializer = CourseListSerializer(courses, many=True)
        return Response({'courses': serializer.data})
