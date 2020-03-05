from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from . forms import TaskForm


#Home function adding show the detail of login clint
@login_required
def index(request):
    user=User.objects.get(username=request.user.username)
    user_task=user.task_set.all()
    if user_task:
        form=TaskForm()
        context={
            "form":form,
            "user_task":user_task
        }
        return render(request,"todos/index.html",context)
    else:
        form=TaskForm()
        context={"form":form}
        messages.info(request,"Please add some wish for today!!")
        return render(request,"todos/index.html",context)



#this function is use for adding todo Item       
@login_required
def add_todo(request):
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            use=form.save(commit=False)
            use.user=request.user
            use.save()
            messages.success(request,"Successfully added a new item")
            return redirect("todos:home")
    else:
        context={"form":form}
        messages.info(request,"Please add some item into list")
        return render(request,"todos/index.html",context)

#this function is used for edit your item
@login_required
def edit(request,pk):
    tsk=get_object_or_404(Task,pk=pk)
    form=TaskForm(instance=tsk)
    if request.method=="POST":
        forms=TaskForm(request.POST,instance=tsk)
        if forms.is_valid():
            usr=forms.save(commit=False)
            usr.save()
            messages.success(request,"Successfully update your list")
            return redirect("todos:home")
    else:
        context={"form":form}
        messages.info(request,"This is a item which you try to update")
        return render(request,"todos/edits.html",context)



#This function is use for delete the item        
@login_required
def delete(request,pk):
    tsk=get_object_or_404(Task,pk=pk)
    tsk.delete()
    messages.success(request,"Successfully delete the item from your list")
    return redirect("todos:home")

#This function is use for complete the particular item
@login_required
def completes(request,pk):
     tsk=get_object_or_404(Task,pk=pk)
     tsk.complete=True
     tsk.save()
     messages.success(request,"Successfully compltete this item from your list")
     return redirect("todos:home")

#This function is use for delete thr complete item
@login_required
def compltete_one(request):
    Task.objects.filter(complete__exact=True).delete()
    messages.success(request,"Successfully delete all complete  item from your list")
    return redirect("todos:home")


#This function is used to delete all the item
@login_required
def delete_all(request):
    Task.objects.all().delete()
    messages.success(request,"Successfully delete all  item from your list")
    return redirect("todos:home")



