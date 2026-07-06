from django.contrib import admin

# Register your models here.
from .models import Voyage, Guest, DiningTable, DiningSession, Reservation, ReservationGuest

admin.site.register(Voyage)
admin.site.register(Guest)
admin.site.register(DiningTable)
admin.site.register(DiningSession)
admin.site.register(Reservation)
admin.site.register(ReservationGuest)