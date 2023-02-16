from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bikes/', include('bikes.urls')),
    path('seia-crawler/', include('seia_crawler.urls')),
]
