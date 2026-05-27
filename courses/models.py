from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(100)
    credits = models.DecimalField(2)

    def __str__(self):
        return self.name
    
