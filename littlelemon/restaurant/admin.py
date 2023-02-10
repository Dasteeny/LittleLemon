from django.contrib import admin
from restaurant.models import Booking, Menu

admin.site.register([Menu, Booking])
