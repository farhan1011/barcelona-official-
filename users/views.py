from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username} , your account is created succesfully')
            return redirect('login')
    else:
         form=UserCreationForm()
    return render(request,'register.html',{'form':form})

