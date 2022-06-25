from django.shortcuts import render,redirect
from .models import Member
from .forms import Memberform
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def users(request):
    all_members = Member.objects.all
    return render(request,'users.html',{'all':all_members})

def signup(request):
    if request.method == "POST":
            form = Memberform(request.POST or None)
            if form.is_valid():
                form.save()
            else:
                fname = request.POST['fname']
                lname = request.POST['lname']
                age = request.POST['age']
                email = request.POST['email']
                passwd = request.POST['passwd']

                messages.success(request,('There was an error trying to submit your form,Please try again!'))
                # return redirect('signup')
                return render(request,'signup.html',{'fname':fname,
                 'lname':lname,
                 'age':age,
                 'email':email,
                 'passwd':passwd,
                })
            messages.success(request,('Your form has been successfully submitted!'))
            return redirect('index')

    else:
        return render(request,'signup.html',{})
