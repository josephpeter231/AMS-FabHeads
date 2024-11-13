# attendance_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
    path('logout/', LogoutView.as_view(next_page='user_dashboard'), name='logout'),
]
