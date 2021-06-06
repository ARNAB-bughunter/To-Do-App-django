from django.shortcuts import render,redirect
from .models import Task

# Create your views here.

def index(request):
	if request.method=='POST':
		task=request.POST['task_data']
		date=request.POST['date']
		data=Task(title=task,due_date=date)
		data.save()
		return redirect('/')	
	return render(request,'index.html',{'tasks':Task.objects.all()})

def delet(request,id):
	Task.objects.get(id=id).delete()
	return redirect('/')

def update(request,id):
	task_name=Task.objects.get(id=id)
	if request.method=='POST':
		task_name.title=request.POST['new_task_data']
		task_name.due_date=request.POST['new_date']
		task_name.save()
		return redirect('/')
	
	return render(request,'update.html',{ 'task':task_name })
