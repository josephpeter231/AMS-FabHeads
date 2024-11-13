# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)

    @property
    def hours_worked(self):
        if self.entry_time and self.exit_time:
            return (self.exit_time - self.entry_time).total_seconds() / 3600
        return 0

class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)
