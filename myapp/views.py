from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
# from BatchProject import settings

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                username=""
                try:
                    unm=newuser.cleaned_data.get(username)
                    print("Username is already exists!")
                    msg="Username is already exists!"
                except usersignup.DoesNotExist:
                    newuser.save()
                    print("Signup Successfully!")
                    msg="Signup Successfully!"
            else:
                print(newuser.errors)
                msg="Error!Something went wrong...Try again!"
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['Password']

            user=usersignup.objects.filter(username=unm,Password=pas)
            uid=usersignup.objects.get(username=unm)
            print("Current UserID:",uid.id)
            if user: #TRUE
                print("Login Successfull!")
                msg="Login Successfull!"
                request.session['user']=unm
                request.session['userid']=uid.id
                return redirect('note')
            else:
                print("Error!Login faild.....")
                msg="Error!Login faild....."
    return render(request,'index.html',{'msg':msg})

def about(request):
    return render (request,'about.html')

def note(request):
    user=request.session.get('user')
    if request.method=='POST':

        newnotes=notesForm(request.POST, request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'note.html',{'user':user})

def contact(request):
    return render (request,'contact.html')

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    uid=usersignup.objects.get(id=userid)
    if request.method=='POST':
        updatereq=updateForm(request.POST,instance=uid)
        if updatereq.is_valid():
            updatereq.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updatereq.errors)
    return render(request,'profile.html',{'user':user,'uid':uid})

def userlogout(request):
    logout(request)
    return redirect('/')