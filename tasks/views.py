from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task, CustomUser, TaskLog
from .forms import UserForm, TaskForm

# Home (Task List)
@login_required
def home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

# Task Detail
@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/view_task.html', {'task': task})

# Register User
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validate password match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')

        # Create user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'tasks/register.html')

# Login User
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'tasks/login.html')

# Logout User
def logout_user(request):
    logout(request)
    return redirect('login')

# Manage Users (Super Admin)
@login_required
def manage_users(request):
    if request.user.role != 'superadmin':
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    users = CustomUser.objects.all()
    return render(request, 'tasks/manage_users.html', {'users': users})

# Update User (Super Admin)
@login_required
def update_user(request, user_id):
    if request.user.role != 'superadmin':
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('manage_users')
    else:
        form = UserForm(instance=user)

    return render(request, 'tasks/update_user.html', {'form': form})

# List Tasks (Admin)
@login_required
def manage_tasks(request):
    if request.user.role not in ['admin', 'superadmin']:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'tasks/manage_tasks.html', {'tasks': tasks})

# Create Task (Admin)
@login_required
def create_task(request):
    if request.user.role not in ['admin', 'superadmin']:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    users = CustomUser.objects.filter(role='user')

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        status = request.POST['status']
        priority = request.POST['priority']
        assigned_to = CustomUser.objects.get(id=request.POST['assigned_to'])

        task = Task.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            assigned_to=assigned_to,
            status=status,
            priority=priority
        )

        messages.success(request, "Task created successfully!")
        return redirect('manage_tasks')

    return render(request, 'tasks/create_task.html', {'users': users})


# Update Task (Admin)
@login_required
def update_task(request, task_id):
    if request.user.role not in ['admin', 'superadmin']:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    task = get_object_or_404(Task, id=task_id)
    users = CustomUser.objects.filter(role='user')

    if request.method == 'POST':
        previous_status = task.status
        previous_priority = task.priority
    
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.start_date = request.POST['start_date']
        task.end_date = request.POST['end_date']
        task.status = request.POST['status']
        task.priority = request.POST['priority']
        task.assigned_to = CustomUser.objects.get(id=request.POST['assigned_to'])
        task.save()

        # Log the update only if status or priority has changed
        if previous_status != task.status or previous_priority != task.priority:
            TaskLog.objects.create(
                task=task,
                updated_by=request.user,
                previous_status=previous_status,
                new_status=task.status,
                previous_priority=previous_priority,
                new_priority=task.priority
            )

        messages.success(request, "Task updated successfully!")
        return redirect('manage_tasks')

    return render(request, 'tasks/update_task.html', {'task': task, 'users': users})

# Delete Task (Admin)
@login_required
def delete_task(request, task_id):
    if request.user.role not in ['admin', 'superadmin']:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('manage_tasks')
