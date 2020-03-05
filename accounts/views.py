from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from . forms import UserLogin,UserSignUp
from django.contrib import messages

#method used for custom login
def login_user(request):
    nexts=request.GET.get("next")
    form=UserLogin()
    if request.method=="POST":
        form=UserLogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            if nexts:
                return redirect(nexts)
            messages.success(request,"successfully login")
            return redirect("todos:home")
            
            
    context={"form":form}
    return render(request,"accounts/login.html",context)

#custom signup method
def signup_user(request):
    nexts=request.GET.get("next")
    form=UserSignUp()
    if request.method=="POST":
        form=UserSignUp(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            new_user=authenticate(username=user.username,password=password)
            login(request,new_user)
            if nexts:
                return redirect(nexts)
            return redirect("accounts:login")
    context={"form":form}
    return render(request,"accounts/signup.html",context)

#custom logout method
def logout_user(request):
    logout(request)
    return redirect("accounts:login")



