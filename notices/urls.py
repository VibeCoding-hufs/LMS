from django.urls import path
from .views import NoticeListView, NoticeDetailView

urlpatterns = [
    path('', NoticeListView.as_view()),
    path('<int:noticeId>/', NoticeDetailView.as_view()),
]
