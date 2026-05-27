from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(100)
    credits = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name
    
