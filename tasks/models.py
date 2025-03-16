from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

# Task Model with Priority
class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('BLOCKED', 'Blocked'),
        ('DONE', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')

    def __str__(self):
        return f"{self.name} - {self.status} - {self.priority}"

class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    previous_status = models.CharField(max_length=20, choices=Task.STATUS_CHOICES)
    new_status = models.CharField(max_length=20, choices=Task.STATUS_CHOICES)
    previous_priority = models.CharField(max_length=10, choices=Task.PRIORITY_CHOICES)
    new_priority = models.CharField(max_length=10, choices=Task.PRIORITY_CHOICES)
    
    def __str__(self):
        return f"Task: {self.task.name} updated by {self.updated_by} at {self.timestamp}"
