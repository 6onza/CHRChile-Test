from django.contrib import admin
from .models import Company, Station

class StationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'latitude', 
        'longitude', 
        'free_bikes', 
        'empty_slots', 
        'timestamp', 
        'address', 
        'altitude', 
        'ebikes', 
        'last_updated', 
        'payment', 
        'payment_terminal', 
        'renting', 
        'returning', 
        'slots'
        )

admin.site.register(Company)
admin.site.register(Station, StationAdmin)