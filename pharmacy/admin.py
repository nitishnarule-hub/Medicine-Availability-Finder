from django.contrib import admin
from .models import Pharmacy, Medicine, Stock

admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(Stock)
