from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import BookForm
from django.urls import reverse
from .filters import PropertyFilter, CityFilter
from django_filters.views import FilterView 




class PropertyList(FilterView):
    model = Property
    paginate_by = 4
    filterset_class = PropertyFilter
    template_name = 'main/property_list.html'
    

class DetailList(FormMixin, DetailView):
    model = Property
    form_class = BookForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category = self.get_object().category)[:3]
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()

            return redirect(reverse('main:property_detail', kwargs={'id': myform.id }))



class AboutView(ListView):
    model = Property
    template_name = "main/about.html"


class ContactView(ListView):
    model = Property
    template_name = "main/about.html"