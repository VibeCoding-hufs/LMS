from django.db import models
from accounts.models import User


class Courses(models.Model):
    name = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # 중복 수강 방지

    def __str__(self):
        return f'{self.user.name} - {self.course.name}'
