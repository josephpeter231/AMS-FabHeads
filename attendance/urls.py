# attendance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('mark_attendance/<int:user_id>/', views.mark_attendance, name='mark_attendance'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('logout/',views.login_view)
]
