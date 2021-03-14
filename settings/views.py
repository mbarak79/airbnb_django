from django.shortcuts import render
from main.models import Property, Place, Category
from django.db.models.query_utils import Q
from django.db.models import Count
# Create your views here.


def index(request):
    places = Place.objects.all().annotate(property_count = Count('property_place'))
    category = Category.objects.all()

    # appartments_list = Property.objects.filter()
    # maisons_list = 
    # villas_list = 
    # hotels_list = 
    context = {
        'places': places,
        'category': category
    }
    return render(request, 'settings/index.html', context )
    



def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    propert_list = Property.objects.filter(
        Q(name__icontains= name) &
        Q(place__name__icontains= place)
    )

    return render(request, 'settings/home_search.html', {'property_list': propert_list})


def category_filter(request,category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    return render(request, 'settings/home_search.html', {'property_list': property_list})