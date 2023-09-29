from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm,CustomAuthenticationForm

def register(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.post)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('dashboard')
    else:
        form=CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form})


def login_view(request):
    if request.method=="POST":
        form=CustomAuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("dashboard") #dashboard url
            
    else:
        form=CustomAuthenticationForm()
    return render(request,'registration/login.html',{'form':form})
    