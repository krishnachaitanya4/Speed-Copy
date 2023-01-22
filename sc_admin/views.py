from django.shortcuts import render,redirect
from orders.models import Orders,OrderDetails
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
# Create your views here.
def panel(request):
    if request.user.is_authenticated:
        return render(request,"panel.html")
    else:
        return redirect(admin_login)

def orders(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            try:
                date = request.GET['date']
                status = request.GET['status']
                print(date,status)
                if status == "Printed":
                    orders = Orders.objects.filter(date=date,delivery_status = status)
                elif status == "Order Received":
                    orders = Orders.objects.filter(date=date,delivery_status = status)
                elif status == "Shipped":
                    orders = Orders.objects.filter(date=date,delivery_status = status)
                elif status == "Delivered":
                    orders = Orders.objects.filter(date=date,delivery_status = status)
                else:
                    orders = Orders.objects.filter(date=date)
                final_list = []
                for i in orders:
                    response = {
                        "id":i.id,
                        "customer_id":str(i.customer_id.id),
                        "date":date,
                        "price":i.total_price,
                        "college":i.college,
                        "status":i.delivery_status
                    }
                    final_list.append(response)
                print(final_list)
                return JsonResponse({'orders':final_list},status=200)
            except:
                pass
        if request.method == 'POST':
            try:
                id = request.POST['id']
                status = request.POST['status']
                order = Orders.objects.get(id=id)
                if status == "Order Received" or status == "Printed" or status == "Shipped" or status == "Delivered":
                    order.delivery_status = status
                    order.save()
                    return JsonResponse({'id':id,'status':status},status = 200)
            except Exception as e:
                pass
        return render(request,'admin_orders.html')
    else:
        return redirect(admin_login)
def admin_login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                auth.login(request,user)
                print("logged in")
                return redirect(panel)
        messages.error(request, 'Invalid cradentials.')
        return redirect(admin_login)
    else:
        return render(request,"admin_login.html")

def manage_orders(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        if request.method == 'GET':
            try:
                date = request.GET['date']
                category = int(request.GET['category'])
                orders = Orders.objects.filter(date=date)
                order_details = []
                if category == 1:
                    for order in orders:
                        details = OrderDetails.objects.filter(order_id =order,product_id = 1)
                        order_details += list(details)
                elif category == 2:
                    for order in orders:
                        details = OrderDetails.objects.filter(order_id =order,product_id = 3)
                        order_details += list(details)
                elif category == 3:
                    for order in orders:
                        details = OrderDetails.objects.filter(order_id =order,product_id = 4)
                        order_details += list(details)
                else:
                    for order in orders:
                        details = OrderDetails.objects.filter(order_id =order)
                        order_details += list(details)
                final_list = []
                for i in order_details:
                    print(i.product_id)
                    response = {
                        'id':i.id,
                        'date':date,
                        'category':str(i.product_id),
                        'copies':i.quantity,
                        'colour':i.colour,
                        'sides':i.sides,
                        'link':str(i.file_upload),
                        'status':i.status
                    }
                    final_list.append(response)
                print(final_list)
                return JsonResponse({"final":final_list},status=200)
            except:
                pass
        if request.method == 'POST':
            id = request.POST.get('id')
            status = request.POST['status']
            if status == "Printed":
                item = OrderDetails.objects.get(id=int(id))
                item.status = "Printed"
                item.save()
            return JsonResponse({'id':id},status = 200)
        return render(request,"manage_orders.html")
    return redirect(admin_login)
