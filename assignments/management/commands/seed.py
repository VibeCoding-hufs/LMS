from django.core.management.base import BaseCommand
from accounts.models import User
from courses.models import Courses, Enrollment
from assignments.models import Assignments
from notices.models import Notice


class Command(BaseCommand):
    help = '더미 데이터 생성 (Users, Courses, Enrollments, Assignments)'

    def handle(self, *args, **kwargs):
        self.stdout.write('더미 데이터 생성 시작...')

        # Users
        users = User.objects.bulk_create([
            User(login_id='prof01', password='1234', name='김교수', email='prof01@lms.com', role='PROFESSOR', dept='컴퓨터공학과'),
            User(login_id='prof02', password='1234', name='이교수', email='prof02@lms.com', role='PROFESSOR', dept='소프트웨어학과'),
            User(login_id='student01', password='1234', name='박학생', email='s01@lms.com', role='STUDENT', dept='컴퓨터공학과'),
            User(login_id='student02', password='1234', name='최학생', email='s02@lms.com', role='STUDENT', dept='컴퓨터공학과'),
            User(login_id='student03', password='1234', name='정학생', email='s03@lms.com', role='STUDENT', dept='소프트웨어학과'),
        ])
        self.stdout.write(f'  Users 생성: {len(users)}개')

        # Courses
        courses = Courses.objects.bulk_create([
            Courses(name='자료구조', credits=3),
            Courses(name='운영체제', credits=3),
            Courses(name='데이터베이스', credits=2),
        ])
        self.stdout.write(f'  Courses 생성: {len(courses)}개')

        # Enrollments (모든 유저가 3개 과목 전부 수강)
        enrollments = []
        for user in users:
            for course in courses:
                enrollments.append(Enrollment(user=user, course=course))
        Enrollment.objects.bulk_create(enrollments)
        self.stdout.write(f'  Enrollments 생성: {Enrollment.objects.count()}개')

        # Assignments (과목별 5개씩)
        assignments = []
        for course in courses:
            for i in range(1, 6):
                assignments.append(
                    Assignments(
                        course=course,
                        title=f'[{course.name}] 과제 {i}번',
                        description=f'{course.name} {i}번째 과제입니다. 기한 내에 제출해주세요.',
                    )
                )
        Assignments.objects.bulk_create(assignments)
        self.stdout.write(f'  Assignments 생성: {Assignments.objects.count()}개')

        # Notices (과목별 3개씩)
        notices = []
        for course in courses:
            for i in range(1, 4):
                notices.append(
                    Notice(
                        course=course,
                        title=f'[{course.name}] 공지사항 {i}번',
                        description=f'{course.name} {i}번째 공지사항입니다. 확인 후 숙지 바랍니다.',
                    )
                )
        Notice.objects.bulk_create(notices)
        self.stdout.write(f'  Notices 생성: {Notice.objects.count()}개')

        self.stdout.write(self.style.SUCCESS('더미 데이터 생성 완료!'))
