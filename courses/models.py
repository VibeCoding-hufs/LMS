from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name
