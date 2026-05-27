from rest_framework import serializers
from .models import Assignments


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = ['id', 'title', 'created_at']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = ['id', 'title', 'description', 'created_at']
