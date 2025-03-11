from django.urls import path
from .views import home, login_user, logout_user, register, task_detail
from .views import (
    manage_users, update_user, 
    manage_tasks, create_task, update_task, delete_task
)

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('task/<int:task_id>/', task_detail, name='task_detail'),

    path('users/', manage_users, name='manage_users'),
    path('users/update/<int:user_id>/', update_user, name='update_user'),
    
    path('tasks/', manage_tasks, name='manage_tasks'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/update/<int:task_id>/', update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]
