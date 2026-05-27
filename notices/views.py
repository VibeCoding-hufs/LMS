from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Notice
from .serializers import NoticeListSerializer, NoticeDetailSerializer


class NoticeListView(ListAPIView):
    serializer_class = NoticeListSerializer

    def get_queryset(self):
        courseId = self.kwargs['courseId']
        return Notice.objects.filter(course_id=courseId)


class NoticeDetailView(APIView):
    def get(self, request, userId, courseId, noticeId):
        notice = get_object_or_404(Notice, id=noticeId, course_id=courseId)
        serializer = NoticeDetailSerializer(notice)
        return Response(serializer.data)
