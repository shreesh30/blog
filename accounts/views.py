from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method=='POST':
        #Login User
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('home')

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

# def dashboard(request):
#     return render(request,'accounts/dashboard.html')

def register(request):
    if request.method=='POST':
        # get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        # check if passwords match
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is being used')
                    return redirect('register')
                
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    # login after register
                    user.save()
                    messages.success(request,'You are now registered and can log')
                    return redirect('login')

        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')