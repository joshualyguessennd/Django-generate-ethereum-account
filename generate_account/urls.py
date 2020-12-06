from . import views
from django.urls import path

urlpatterns = [
    path('', views.generate_random_address, name='address')
]