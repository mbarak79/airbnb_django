from django.urls import path
from .views import index, home_search, category_filter

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('search', home_search, name='home_search'),
    path('category/<slug:category>', category_filter, name='category_filter')
    
    
]