from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
def LoginUser(request):

    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,login)
                return redirect('index')
    else:
        form= LoginUserForm()

    return render(request, 'login.html',{'form':form})

def RegisterUser(request):

    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            # user = User.objects.create_user(
            # username = form.cleaned_data['username'], 
            # first_name = form.cleaned_data['first_name'], 
            # last_name = form.cleaned_data['last_name'], 
            # email = form.cleaned_data['email'],
            # password = form.cleaned_data['password'] 
            # )
            # user.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'login.html',{'form':form})
