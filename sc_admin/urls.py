from django.urls import path
from . import views

urlpatterns = [
    path("",views.panel,name="panel"),
    path("orders",views.orders,name="manage-orders"),
    path("login",views.admin_login,name="admin-login")
]