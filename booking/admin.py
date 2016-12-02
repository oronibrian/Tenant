from hvad.admin import TranslatableAdmin

from . import models
from django.contrib import admin

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'creation_date', 'booking_status', 'booking_id', 'user', 'email',
        'session', 'date_from', 'date_until',
    ]


class BookingItemAdmin(admin.ModelAdmin):
    list_display = ['booking', 'booked_item', 'quantity', 'persons']


admin.site.register(models.Booking, BookingAdmin)
admin.site.register(models.BookingError)
admin.site.register(models.BookingItem, BookingItemAdmin)
admin.site.register(models.BookingStatus, TranslatableAdmin)
admin.site.register(models.ExtraPersonInfo)
