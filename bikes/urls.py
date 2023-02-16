from django.urls import path
from .views import SaveBikesDataView, BikesDataView


urlpatterns = [
    path('save-bikes-data/', SaveBikesDataView.as_view(), name='save_bikes_data'),
    path('bikes-data/', BikesDataView.as_view(), name='bikes_data'),
]