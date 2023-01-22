from django.urls import path
from . import views
urlpatterns = [
    path("cart",views.cart,name="cart"),
    path("<int:pk>",views.view,name = "order_details"),
    path("orders",views.orders,name="orders"),
    path("add_to_cart",views.add_to_cart,name="add_to_cart"),
    path("delete",views.delete,name="delete"),
    path("checkout",views.checkout,name='checkout'),
    path("payment",views.payment,name='payment'),
    path("confirm_order",views.confirm_order,name="confirm_order"),
]
