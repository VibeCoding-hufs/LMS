from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('accounts/', include('accounts.urls')),
    path('<int:userId>/courses/', include('courses.urls')),
    path('<int:userId>/courses/<int:courseId>/notices/', include('notices.urls')),
    path('<int:userId>/courses/<int:courseId>/assignments/', include('assignments.urls')),
]
