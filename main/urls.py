from django.urls import path
from .views import PropertyList, DetailList

app_name = 'property'

urlpatterns = [
    path('property/', PropertyList.as_view(), name='property'),
    path('<slug:slug>', DetailList.as_view(), name='property_detail')
    
]