from django.urls import path
from . import views

urlpatterns = [
    path("login",views.staff_login,name="staff-login"),
    path("orders",views.orders,name="view-orders")
]