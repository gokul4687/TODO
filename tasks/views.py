from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# HOME – List all tasks
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# ADD task
def add_task(request):
    if request.method == 'POST':
        Task.objects.create(
            subject=request.POST['subject'],
            notes=request.POST['notes']
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

# EDIT task ✅ (THIS WAS MISSING BEFORE)
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.subject = request.POST['subject']
        task.notes = request.POST['notes']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

# VIEW task
def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_view.html', {'task': task})

# DELETE task
def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('task_list')
