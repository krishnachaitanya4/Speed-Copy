from django.contrib import admin
from .models import Address
admin.site.site_header = "SpeedCopy Administration"
# Register your models here.
admin.site.register(Address)