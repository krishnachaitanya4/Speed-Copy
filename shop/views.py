from django.shortcuts import render,redirect

# Create your views here.
def shop(request):
    return render(request,'product.html')

def cart(request):
    return redirect("account/cart")