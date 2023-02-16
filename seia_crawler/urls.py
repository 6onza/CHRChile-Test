from django.urls import path
from .views import StoreProjectsView, ProjectsView

urlpatterns = [
    path('store-projects-data/', StoreProjectsView.as_view(), name='store_projects'),
    path('projects/', ProjectsView.as_view(), name='projects'),
]