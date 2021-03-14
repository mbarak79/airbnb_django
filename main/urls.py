from django.urls import path
from .views import PropertyList, DetailList, AboutView, ContactView

app_name = 'property'

urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('property', PropertyList.as_view(), name='property'),
    path('<slug:slug>', DetailList.as_view(), name='property_detail')
    
]