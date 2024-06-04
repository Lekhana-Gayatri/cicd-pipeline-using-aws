from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def sign_in(request):
    if request.method=='POST':
        email=request.POST['mail']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            print(user.username)
            return redirect('/index/')
    return render(request,'sign-in.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def sign_up(request):
    if request.method=='POST':
        lastname=request.POST['lastName']
        firstname=request.POST['firstName']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmPassword']
        if password is not confirmpassword:
            redirect('/login/')
        user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password,username=email)
        user.save()
    return render(request,'sign-up.html')

def reset_password(request):
    if request.method=="POST":
        mail=request.POST['mail']
        send_email(mail)
        return redirect('/login/')
    return render(request,'password-forget.html')

def start(request,category=None):
    return render(request,'sign-up.html')



from django.core.mail import send_mail
from django.conf import settings
def send_email(mail):
    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    send_mail(subject, message, 'settings.EMAIL_HOST_USER', [mail],fail_silently=False)


@login_required(login_url="/login/")
def create_fundraiser(request):
    if request.method == 'POST':
        data=request.POST
        username=request.user
        category=data.get('category')
        fund_for=data.get('type')
        goal=data.get('amount')
        photo=request.FILES.get('formFile')
        title=data.get('title')
        story=data.get('story')
        phone=data.get('phone')
        fundraiser = fundRaised.objects.create(username=username,category=category,fund_for=fund_for,goal=goal,photo=photo,title=title,story=story,phone=phone)
        return redirect('/login/')
    return render(request, 'donation.html')
    
def showFundDetails(request,id):
    if request.method=='GET':
        f=fundRaised.objects.get(pk=id)
        percent_covered=(f.present_fund/f.goal)*100
        context={'f':f,'percent':percent_covered}
        return render(request,'showDetails.html',context=context)

def donate(request,id):
    if request.method=='POST':
        pass
    return render(request,'donate.html')

