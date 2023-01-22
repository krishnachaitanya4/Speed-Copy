from django.shortcuts import render,redirect
from shop.models import Products
from .models import Cart,Orders,OrderDetails,Payments
from django.contrib import messages
from account.models import Address
from django.http import Http404
import PyPDF2
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import auth, User
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
import razorpay
from .price import *
# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        products = Cart.objects.filter(user_id=user)  
        context ={
            'products':products,
            'total_price':sum([i.price for i in products])
            }
        #print("cart",context)
        return render(request,"cart.html",context)
    else:
        return render(request,"login.html")

def orders(request):
    user = request.user
    if user.is_authenticated:
        orders = list(Orders.objects.filter(customer_id = user))
        return render(request,"orders.html",{'orders':orders})

def view(request,pk):
    if request.user.is_authenticated:
        try:
            order = Orders.objects.get(id=pk)
            details = OrderDetails.objects.filter(order_id = pk)
            payment = Payments.objects.get(id=pk)
            return render(request,'view.html',{'order':order,'details':details,'payment_id':payment.payment_id})
        except:
            return redirect('orders')
    return(render,"index.html")

def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                product_name = request.POST['product_name']
                if product_name == "Spiral Binding":
                    pdf_file = request.FILES['pdf_file']   
                    sided = int(request.POST['sides'])
                    colour = int(request.POST['colour'])
                    copies = int(request.POST['copies'])
                    try:
                        pdfReader = PyPDF2.PdfFileReader(pdf_file)
                        pages = pdfReader.numPages
                    except:
                        messages.error(request,"Only .pdf files are accepted")
                        return render(request,'product.html',context={'name':'spiral_binding'})
                    price = get_price_spiral_binding(pages,sided,colour,copies)
                    product = Products.objects.filter(name=product_name)[0]
                    user = request.user
                    cart_item = Cart(user_id=user,product_id=product,file_upload=pdf_file,pages=pages,sides=sided,quantity=copies,colour=colour,price=price)
                    cart_item.save()

                elif product_name == "Record Binding":
                    pdf_file = request.FILES['pdf_file']
                    copies = int(request.POST['copies'])
                    try:
                        pdfReader = PyPDF2.PdfFileReader(pdf_file)
                        pages = pdfReader.numPages
                    except:
                        messages.error(request,"Only .pdf files are accepted")
                        return render(request,'product.html',context={'name':product_name})
                    price = get_price_record_printing(pages,copies)
                    product = Products.objects.filter(name=product_name)[0]
                    user = request.user
                    cart_item = Cart(user_id=user,product_id=product,file_upload=pdf_file,pages=pages,quantity=copies,price=price)
                    cart_item.save()

                elif product_name == "printing":
                    pdf_file = request.FILES['pdf_file']
                    sided = int(request.POST['sides'])
                    colour = int(request.POST['colour'])
                    copies = int(request.POST['copies'])

                    try:
                        pdfReader = PyPDF2.PdfFileReader(pdf_file)
                        pages = pdfReader.numPages
                    except:
                        messages.error(request,"Only .pdf files are accepted")
                        return render(request,'product.html',context={'name':product_name})
                    price = float(request.POST['price'])
                    price = get_price_printing(pages,sided,colour,copies)
                    product = Products.objects.filter(name=product_name)[0]
                    user = request.user
                    cart_item = Cart(user_id=user,product_id=product,file_upload=pdf_file,pages=pages,sides=sided,quantity=copies,colour=colour,price=price)
                    cart_item.save()

                elif product_name == "3D Printing":
                    pdf_file = request.FILES['pdf_file']
                    pages = int(request.POST['pages'])
                    copies = int(request.POST['copies'])
                    price = request.POST['price']
                    product = Products.objects.filter(name=product_name)[0]
                    user = request.user
                    cart_item = Cart(user_id=user,product_id=product,file_upload=pdf_file,pages=pages,quantity=copies,price=price)
                    cart_item.save()
                else:
                    raise Http404("Page not found :(")

                messages.success(request, "Item added to the cart" )
                return redirect("cart")
            except:
                return render(request,"product.html",{'name':product_name})
        else:
            return render(request,"login.html")
    raise Http404("page not found!!!")


def delete(request):
    try:
        if request.method == 'POST':
            p_id = request.POST['p_id']
            Cart.objects.filter(id=p_id).delete()
            messages.warning(request, 'Item has been deleted from your cart!!!')
    except:
        return redirect(cart)
    return redirect('cart')

def checkout(request):

    if request.user.is_authenticated:
        user = request.user
        products = Cart.objects.filter(user_id=user)  
        pr = sum([i.price for i in products])
        context ={
            'products':products,
            'total_price':pr,
            'no_of_products':len([i for i in products]),
            'p2': pr*100,
            }
        if context['total_price'] == 0:
            return redirect("cart")

    return render(request,"checkout.html",context)


@csrf_exempt
def confirm_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            payment_id = request.POST["razorpay_payment_id"]
            order_id = request.POST["razorpay_order_id"]
            signature = request.POST["razorpay_signature"]
            # Generating signature
            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
            status = client.utility.verify_payment_signature({
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            })
            info = client.order.fetch(order_id)
            total_price = float(info['amount_paid'])/100
            address = info['notes']['address']
            if status == True:
                user = request.user
                products = Cart.objects.filter(user_id=user)  
                order = Orders.objects.create(customer_id = user,payment_status=True,total_price = total_price,college=address)
                order.save()
                payment = Payments.objects.create(id=order,order_id=order_id,payment_id=payment_id,signature=signature)
                payment.save()
                for i in products:
                    order_details = OrderDetails.objects.create(order_id=order,product_id=i.product_id,file_upload=i.file_upload,pages=i.pages,quantity=i.quantity,colour=i.colour,sides=i.sides,sub_total=i.price,status="Pending")
                    order_details.save()
                products.delete()
                u = User.objects.filter(username = user)[0]
                '''
                mydict = {
                    'username': u.first_name+" "+u.last_name,
                    'products': products,
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
                
                '''
            return render(request,'invoice.html')
        raise Http404("Page Not Found :(")
    raise Http404("Page Not Found :(")

def payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f_name = request.POST.get('f_name')
            l_name = request.POST.get("l_name")
            email = request.POST.get('email')
            college = request.POST.get('college')
            user = request.user
            u = User.objects.filter(username=user)
            u = u[0]
            products = Cart.objects.filter(user_id=user)  
            print([i.product_id for i in products],"\nzzzzzzzzzzzzz\n")
            context ={
                'products':products,
                'total_price':sum([i.price for i in products])
                }
            # Payment integration
            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
            DATA = {
                "amount": context['total_price']*100,
                "currency": "INR",
                "payment_capture":"1",
                "notes": {
                    "address":college
                }
            }
            payment_order = client.order.create(data=DATA)
            print("college ====>",college)
           
            print(products)
            
            context ={
                'products':products,
                'total_price':sum([i.price for i in products])
                }
            mydict = {
                'username': u.first_name+" "+u.last_name,
                'products': products,
                'price':context['total_price']*100
            }

            print("xxxxxxxxxxxxxxxxxxx\n",payment_order,"\nxxxxxxxxxxxxxxxxxxx\n")
            phone = Address.objects.filter(user_id=u)
            phone = phone[0]
            phone = phone.phone
            return render(
                request,
                "payment.html",
                {
                    "callback_url": "http://" + "127.0.0.1:8000" + "/orders/confirm_order",
                    "razorpay_key": settings.RAZORPAY_API_KEY,
                    "order_id":payment_order['id'],
                    "price":mydict['price'],
                    "phone":phone,
                    "college":college,
                }
            )
        else:
            return render(request,'checkout.html')

#------------------------------END---------------------------------------------#