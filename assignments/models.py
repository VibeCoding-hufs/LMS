from django.db import models
from courses.models import Courses


class Assignments(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
