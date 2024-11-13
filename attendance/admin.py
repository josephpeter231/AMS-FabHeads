# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Attendance, LeaveRequest

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'is_admin', 'is_active']
    list_filter = ['is_admin', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'entry_time', 'exit_time', 'hours_worked']
    list_filter = ['user', 'entry_time']
    readonly_fields = ['hours_worked']

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'reason', 'approved']
    list_filter = ['approved', 'user']
    actions = ['approve_leave', 'reject_leave']

    def approve_leave(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected leave requests have been approved.")

    def reject_leave(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, "Selected leave requests have been rejected.")

    approve_leave.short_description = "Approve selected leave requests"
    reject_leave.short_description = "Reject selected leave requests"
