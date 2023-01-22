from django.shortcuts import render,redirect
from requests import request
from django.contrib.auth.models import User,auth
from account.models import Address
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("logged in")
            return redirect("/")
        else :
            print("wrong password")
            messages.error(request, 'Invalid cradentials.')
            return redirect(login)
    else:
        return render(request,"login.html")



def register(request):
    try:
        if request.method == 'POST':
            first_name = request.POST['f_name']
            last_name = request.POST['l_name']
            if first_name=='' or last_name == '':
                messages.error(request,"! Please fill all fields.")
                return redirect(register)
            email = request.POST['email'] 
            if User.objects.filter(email=email).exists():
                messages.error(request,"! Email already in use.")
                return redirect(register)
            phone = request.POST['phone']
            password = request.POST['password']
            confirm_password = request.POST['password2']
            if password != confirm_password:
                messages.error(request,"! Passwords didn't match.")
                return redirect(register)
            user = User.objects.create_user(first_name = first_name,last_name=last_name,email=email,password=password,username = email)
            user.save()
            address = Address.objects.create(user_id=user,phone=phone)
            address.save()
            messages.success(request,"Account created successfully.")
            return redirect("login")
        return render(request,'register.html')
    except:
        return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
