from django.shortcuts import render
import requests
from .models import Company, Station
from django.views.generic import View
from .utils import get_bike_data
from django.http import HttpResponse
import datetime


class SaveBikesDataView(View):
    def get(self, request):
        data = get_bike_data()
        if not data:
            return HttpResponse('Error!', status=500)

        company_name = data['network']['company'][0]
        company, created = Company.objects.get_or_create(
            name=company_name,
            defaults={'gbfs_href': data['network']['gbfs_href']}
        )

        for station in data['network']['stations']:
            Station.objects.create(
                company=company,
                name=station['name'],
                latitude=station['latitude'],
                longitude=station['longitude'],
                free_bikes=station['free_bikes'],
                empty_slots=station['empty_slots'],
                timestamp=station['timestamp'],
                address=station['extra']['address'],
                altitude=station['extra']['altitude'],
                ebikes=station['extra']['ebikes'],
                has_ebikes=station['extra']['has_ebikes'],
                last_updated=station['extra']['last_updated'],
                payment=', '.join(station['extra']['payment']),
                payment_terminal=station['extra']['payment-terminal'],
                renting=station['extra']['renting'],
                returning=station['extra']['returning'],
                slots=station['extra']['slots'],
            )

        return HttpResponse('Data saved!', status=200)



class BikesDataView(View):
    def get(self, request):
        stations = Station.objects.all()
        return render(request, 'bikes_info.html', {'stations': stations})

