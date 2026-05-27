from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Assignments
from .serializers import AssignmentListSerializer, AssignmentDetailSerializer


class AssignmentListView(APIView):
    def get(self, request, userId, courseId):
        assignments = Assignments.objects.filter(course_id=courseId).order_by('-created_at')[:10]
        serializer = AssignmentListSerializer(assignments, many=True)
        return Response({'assignments': serializer.data})


class AssignmentDetailView(APIView):
    def get(self, request, userId, courseId, assignmentId):
        try:
            assignment = Assignments.objects.get(id=assignmentId, course_id=courseId)
        except Assignments.DoesNotExist:
            raise NotFound('과제를 찾을 수 없습니다.')
        serializer = AssignmentDetailSerializer(assignment)
        return Response(serializer.data)
