from django.urls import path
from assignments import views

urlpatterns = [
    path('', views.AssignmentListView.as_view(), name='assignment-list'),
    path('<int:assignmentId>/', views.AssignmentDetailView.as_view(), name='assignment-detail'),
]
