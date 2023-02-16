from django.urls import path
from .views import SaveBikesDataView, BikesDataView


urlpatterns = [
    path('store-bikes-data/', SaveBikesDataView.as_view(), name='store_bikes_data'),
    path('bikes-stations/', BikesDataView.as_view(), name='bikes_stations'),
]