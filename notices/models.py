from django.db import models
from courses.models import Courses

# Create your models here.
class Notice(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='notices')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']