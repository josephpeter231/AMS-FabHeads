# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User, Attendance, LeaveRequest
from .forms import UserRegistrationForm, AttendanceForm, LeaveRequestForm
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def admin_dashboard(request):
    if request.user.is_admin:
        users = User.objects.all()
        return render(request, 'admin_dashboard.html', {'users': users})
    return redirect('user_dashboard')

@login_required
def user_dashboard(request):
    if not request.user.is_admin:
        attendance_records = Attendance.objects.filter(user=request.user)
        leave_requests = LeaveRequest.objects.filter(user=request.user)
        return render(request, 'user_dashboard.html', {
            'attendance_records': attendance_records,
            'leave_requests': leave_requests
        })
    return redirect('admin_dashboard')

@login_required
def mark_attendance(request, user_id):
    if request.user.is_admin:
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            form = AttendanceForm(request.POST)
            if form.is_valid():
                attendance = form.save(commit=False)
                attendance.user = user
                attendance.save()
                return redirect('admin_dashboard')
        else:
            form = AttendanceForm()
        return render(request, 'mark_attendance.html', {'form': form, 'user': user})
    return redirect('user_dashboard')

@login_required
def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = request.user
            leave_request.save()
            return redirect('user_dashboard')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_request.html', {'form': form})
