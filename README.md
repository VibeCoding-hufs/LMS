# LMS (Learning Management System)

한국외국어대학교 eClass를 참고하여 설계한 학습 관리 시스템입니다.

## 기술 스택

- **Backend**: Django 6.0.5
- **Database**: SQLite
- **Language**: Python 3.13

## 프로젝트 구조

```
LMS/
├── accounts/       # 사용자, 학과
├── courses/        # 강좌, 과목, 수강신청, 강의계획서
├── assignments/    # 과제, 제출
├── teams/          # 팀프로젝트, 팀, 팀원, 팀제출
├── contents/       # 강의자료, 공지사항
├── config/         # Django 설정
├── sql/
│   └── schema.sql  # DB 스키마
└── manage.py
```

## 도메인별 테이블

| 앱 | 테이블 |
|----|--------|
| accounts | Users, Departments |
| courses | Courses, Subjects, Enrollments, Syllabuses |
| assignments | Assignments, Submissions |
| teams | TeamProjects, Teams, TeamMembers, TeamSubmissions |
| contents | CourseContents |

## 시작하기

### 1. 저장소 클론

```bash
git clone https://github.com/victorlee02/LMS.git
cd LMS
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Mac / Linux
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 서버 실행

```bash
python manage.py migrate
python manage.py runserver
```

## 팀원

| 이름 | GitHub |
|------|--------|
| 이정현 | [@victorlee02](https://github.com/victorlee02) |
| 김대환 | [@kdh635899-ops](https://github.com/kdh635899-ops) |
| 이현정 | [@GNAchoux](https://github.com/GNAchoux) |
