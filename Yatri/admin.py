from django.contrib import admin
from .models import RegistrationData

admin.site.site_header='Admin Dashboards'

# Register your models here.
admin.site.register(RegistrationData)

