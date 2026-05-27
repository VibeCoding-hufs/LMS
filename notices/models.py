from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']