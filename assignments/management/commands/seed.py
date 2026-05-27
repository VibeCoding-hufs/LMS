from django.core.management.base import BaseCommand
from accounts.models import User
from courses.models import Courses
from assignments.models import Assignments


class Command(BaseCommand):
    help = '더미 데이터 생성 (Users, Courses, Assignments)'

    def handle(self, *args, **kwargs):
        self.stdout.write('더미 데이터 생성 시작...')

        # Users
        users = [
            User(login_id='prof01', password='1234', name='김교수', email='prof01@lms.com', role='PROFESSOR', dept='컴퓨터공학과'),
            User(login_id='prof02', password='1234', name='이교수', email='prof02@lms.com', role='PROFESSOR', dept='소프트웨어학과'),
            User(login_id='student01', password='1234', name='박학생', email='s01@lms.com', role='STUDENT', dept='컴퓨터공학과'),
            User(login_id='student02', password='1234', name='최학생', email='s02@lms.com', role='STUDENT', dept='컴퓨터공학과'),
            User(login_id='student03', password='1234', name='정학생', email='s03@lms.com', role='STUDENT', dept='소프트웨어학과'),
        ]
        User.objects.bulk_create(users)
        self.stdout.write(f'  Users 생성: {User.objects.count()}개')

        # Courses
        courses = [
            Courses(name='자료구조', credits=3),
            Courses(name='운영체제', credits=3),
            Courses(name='데이터베이스', credits=2),
        ]
        Courses.objects.bulk_create(courses)
        self.stdout.write(f'  Courses 생성: {Courses.objects.count()}개')

        # Assignments (과목별 5개씩)
        assignments_data = []
        for course in Courses.objects.all():
            for i in range(1, 6):
                assignments_data.append(
                    Assignments(
                        course=course,
                        title=f'[{course.name}] 과제 {i}번',
                        description=f'{course.name} {i}번째 과제입니다. 기한 내에 제출해주세요.',
                    )
                )
        Assignments.objects.bulk_create(assignments_data)
        self.stdout.write(f'  Assignments 생성: {Assignments.objects.count()}개')

        self.stdout.write(self.style.SUCCESS('더미 데이터 생성 완료!'))
