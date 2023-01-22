from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("account_details",views.account_details,name="account_details"),
    path("printing/",views.printing,name='printing'),
    path("printing_3d/",views.printing_3d,name='printing_3d'),
    path("record_binding/",views.record_binding,name='record_binding'),
    path("spiral_binding/",views.spiral_binding,name='spiral_binding'),
    path("send",views.send_email,name='send_mail'),
    path("show_email",views.show_email,name="show_email")
]