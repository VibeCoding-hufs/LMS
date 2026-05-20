from django.db import models


class User(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', '학생'
        PROFESSOR = 'PROFESSOR', '교수'
        ADMIN = 'ADMIN', '관리자'

    login_id = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    dept = models.CharField(max_length=50, blank=True, null=True)