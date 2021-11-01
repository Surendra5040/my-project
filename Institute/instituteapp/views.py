from django.shortcuts import render,redirect
from .models import contact,Feedback
from .form import registerform
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def Home(request):
    return render(request,'home.html')

def contacts(request):
    if request.method=='GET':
        return render(request,'contact.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')

        contact(
            name=name,
            email=email,
            query=query
        ).save()
        return render(request, 'contact.html')


def services (request):
    return render(request,'services.html')

def feedback(request):
    if request.user.is_authenticated:
        if request.method=='GET':
            feedbacks=Feedback.objects.all()
            return render(request,'feedback.html',{'feedbacks':feedbacks})
        else:
            name=request.POST.get('name')
            feedback=request.POST.get('feedback')

            Feedback(
                name=name,feedback=feedback
            ).save()
            feedbacks = Feedback.objects.all()
            return render(request, 'feedback.html',{'feedbacks':feedbacks})
    else:
        return redirect('login')

def gallery(request):
    return render(request,'gallery.html')

def registers(request):
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirmPassword=request.POST.get('confirmPassword')
            if password==confirmPassword:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'username already exists')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.warning(request, 'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=confirmPassword,
                                                    email=email
                                                    )
                    user.save();




            else:
                messages.warning(request, 'password missmatch')
                return redirect('register')


            return redirect('home')

    else:
        form=registerform()
        return render(request,'register.html',{'form':form})

def logging(request):
    if request.method=="POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request, 'user is not active')
                return redirect('register')
        else:
            messages.warning(request,'Incorrect password or username')
            return redirect('login')
    else:
        return render(request,'login.html')
def user_log_out(request):
    logout(request)
    return redirect('home')

