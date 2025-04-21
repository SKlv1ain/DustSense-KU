from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.api_data, name='api-data'),
    path('statistics/', views.statistics, name='statistics'),
]


