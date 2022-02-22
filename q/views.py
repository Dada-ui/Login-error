from django.contrib import messages
from django.shortcuts import redirect, render
from q.models import *
from q.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def cover(request):
    return render(request,'cover.html')

@login_required
def home(request):
    """h = Register_model.objects.filter(username='username')
    if h is not None:
        messages.warning(request,'please login')
        return redirect('login')
    messages.success(request,'Login successfullyyyyy')"""
    return render(request,'home.html',{})


def services(request):
    return render(request,'services.html')


def about(request):
    return render(request,'about.html')


def contactview(request):
    form = Contact_form()
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thanks for contacting us.. Have a nice day...!!!')
    return render(request,'contact.html')
    

def loginview(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        a = authenticate(username=username,password=password)
        if a:
            print(a)
            login(request,a)
            messages.success(request,'Login Successfully..!')
            return redirect('home')
    return render(request,'login.html')


def registerview(request):
    form = Register_form()
    if request.method == 'POST':
        form = Register_form(request.POST)

        # Checking Already Data Has Been Recorded or Not..!

        # Username
        if Register_model.objects.filter(username = request.POST['username']):
            messages.warning(request,'Username already exists')

        # Phone Number
        elif Register_model.objects.filter(phone = request.POST['phone']):
            messages.warning(request,'Phone number already exists')

        # Re - Phone Number
        elif Register_model.objects.filter(rephone = request.POST['rephone']):
            messages.warning(request,'Phone number not same')

        # Email
        elif Register_model.objects.filter(email = request.POST['email']):
            messages.warning(request,'Email address already exists')

        # Re - Email
        elif Register_model.objects.filter(reemail = request.POST['reemail']):
            messages.warning(request,'Email address not same')
            return render(request,'register.html', {'rf':form})

        if form.is_valid():
            form.save()
            messages.success(request,'New Account Has Created Successfully - Please Login Now..!')
            return redirect('login')
    return render(request,'register.html',{'form':form})


def logoutview(request):
    return render(request,'logout.html')


def profile_edit(request):
    return render(request,'profile_edit.html')


def accountview(request):
    return render(request,'account.html')