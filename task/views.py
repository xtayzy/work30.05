from django.shortcuts import render
import re

# Create your views here.
from task.models import TaskList


def index(request):
    tasks = TaskList.objects.all()

    task = TaskList(
        title='task '
    )
    task.save()

    # for i in range(2, 10):
    #     task = TaskList(
    #         title=f'task {i}'
    #     )
    #     task.save()

    # for task in tasks:
    #     task.title = f'{task.title}, id:{task.id}'
    #     task.save()

    for task in tasks:
        if re.search(r'\d', task.title):
            task.delete()

    ctx = {
        'tasks': tasks
    }

    return render(request, 'task/index.html', ctx)

