from django.shortcuts import render,redirect
from orders.models import Orders,OrderDetails
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def orders(request):
    user = request.user
    print(user.is_superuser)
    if user.is_superuser or user.is_staff:
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
        return render(request,"view_orders.html")
    return redirect(staff_login)
def staff_login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        print(user)
        if user is not None:
            if user.is_superuser or user.is_staff:
                auth.login(request,user)
                print("logged in")
                return redirect(orders)
        messages.error(request, 'Invalid cradentials.')
        return redirect(staff_login)
    else:
        return render(request,"staff_login.html")

