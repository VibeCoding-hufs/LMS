## 프로젝트 개요

- 서비스명: HelloLMS
- 목적: LMS 기능 일부 구현, 간단한 클론 코딩

### 도메인

#### 기본 도메인

- Users
- Courses

#### Courses 관련

- Subjects : 상위 도메인, 개설과 별개로 기본 설정된 교과목 정보
- Enrollments : 다수의 Users가 다수의 Courses에 등록하기 위해 연결된 도메인
- Users : LMS에 가입된 회원을 통합 관리하는 도메인. 교수 / 학생 / 관리자로 구분됨.
- Syllabuses : Courses에 대한 강의계획서
- CourseContents : 교수가 Courses 객체에서 업로드하는 게시글. 공지사항 / 강의자료로 구분됨.
- TeamProjects : course에 소속된 팀프로젝트 최상위 카테고리.
    - Teams : 여러 팀을 모아볼 수 있는 도메인.
        - TeamMembers: Team마다 소속된 수강생(user)를 관리하는 도메인. Users를 상속
    - TeamSubmissions : 팀프로젝트 결과물/제출물을 관리하는 도메인.
- Assignments : course에서 제시된 과제물을 관리하는 도메인.
    - Submissions : 과제물/제출물을 관리하는 도메인. Users를 상속

## 기술 스택

- Python
- Django
- Django REST Framework

## 프로젝트 구조

LMS/
├── config/ # asgi.py, settings.py, urls.py, wsgi.py
├── accounts/
├── assignments/
├── contents/
├── courses/
├── subjects/
├── teams/
└── requirements.txt

Django - 가상환경 - 실행

## 코딩 컨벤션

@.claude/rules/convention.md

## 인증

- 인증 없음.

## API 설계 원칙

- Courses 관련 로직은 /course/{course_id}로 시작

## 주의 사항

@.claude/rules/notanda.md

## 테스트

- 코드 구현 시 반드시 테스트 확인

## 커밋 컨벤션

.claude/rules/commit.md
