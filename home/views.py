from django.shortcuts import render
from requests import request
from django.contrib.auth.models import auth,User
from django.contrib import messages
from shop.models import Products
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    return render(request,"index.html")
def account_details(request):
    return render(request,"account2.html")
def printing(request):
    product = Products.objects.filter(name = "printing").values()
    dic = product[0]
    print(dic)
    return render(request,"product.html",{"pro":dic,"name":"printing"})

def printing_3d(request):
    product = Products.objects.filter(name = "3D Printing").values()
    dic = product[0]
    print(dic)
    return render(request,"product.html",{"pro":dic,"name":"printing_3d"})

def record_binding(request):
    product = Products.objects.filter(name = "Record Binding").values()
    dic = product[0]
    print(dic)
    return render(request,"product.html",{"pro":dic,"name":"record_binding"})

def spiral_binding(request):
    product = Products.objects.filter(name = "Spiral Binding").values()
    dic = product[0]
    print(dic)
    return render(request,"product.html",{"pro":dic,"name":"spiral_binding"})

def send_email(request):
    if request.method == 'POST':
        u = request.user
        email =  request.user.email
        status = send_mail(
            'Testing mail',
            'This is a testing mail',
            'krishnachaitanya055@gmail.com',
            [email],
            fail_silently=False
        )
        mydict = {
                'username':'krishna chaitanya',
                }
        html_template = 'confirmation_email.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = "We've received your order"
        email_from = settings.EMAIL_HOST_USER
        print(u.email)
        recipient_list = [u.email]
        message = EmailMessage(subject, html_message,
                                        email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
                
        print(status)   

        print(email)
    return render(request,'email.html')

def show_email(request):
    return render(request,'confirmation_email.html')