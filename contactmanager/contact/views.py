from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
    


# Create your views here.
def signup (request):
    form = SignupForm(request.POST or None)
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        
        
        if password == password2:
            try:
                user = User.objects.create_user(username ,  email , password )
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            except:
                user = None
        
            if user != None:
                login(request , user)
                return redirect ('home')
            else:
                request.session['register_error'] = 1
    context = {'form':form}
    return render(request , 'signup.html', context)


def signin(request):
    form = SigninForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('home')
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request , username=username , password=password)
        if user != None:
            login(request,user)
            return redirect('home')
        else:
            request.session['invalid_user'] = 1
    context = {'form':form}
    return render(request , 'signin.html', context) 


@login_required(login_url = 'signin')
def signout (request):
    logout(request)
    return redirect('home')
    

@login_required(login_url='signin')
def home (request):
    return render(request,'home.html')     
        
# @login_required(login_url='signin')
def addcontact(request):
    form = AddContactForm()
    
    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            contact = Contact(
                user = request.user,
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                email = cd['email'],
                mobile = cd['mobile'],
                alternate_number = cd['alternate_number'],
                )
            contact.save()
            return redirect ('home')
    context = {'form':form}
    return render (request , 'addcontact.html' , context)
        
        
        
               
               
                 
        
        
        