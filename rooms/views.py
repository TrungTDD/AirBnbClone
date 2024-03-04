from math import ceil
from urllib import parse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage
from django.views.generic import ListView, DetailView, TemplateView

from django_countries import Countries

from .models import Room, RoomType, Amenity
from . import forms


class ListRooms(ListView):
    model = Room
    paginate_by = 10


class RoomDetail(DetailView):
    model = Room


class SearchView(TemplateView):
    template_name = "rooms/search.html"
    
    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        country = self.request.GET.get("country")
        
        if country:
            form = forms.SearchForm(self.request.GET)
            if form.is_valid():
                city = form.cleaned_data["city"]
                country = form.cleaned_data["country"]
                amenities = form.cleaned_data["amenity"]
                instant_book = form.cleaned_data["instant_book"]
                superhost = form.cleaned_data["superhost"]

                queryset = Room.objects.filter()
                filters = {}
                parameters = {}

                if city:
                    filters["city__startswith"] = city
                    parameters['city'] = city

                if country:
                    filters["country"] = country
                    parameters['country'] = country

                if amenities:
                    for amenity in amenities:
                        queryset = queryset.filter(amenities=amenity)
                        if not parameters.get('amenity'):
                            parameters['amenity'] = []

                        parameters['amenity'].append(amenity.pk)

                queryset = queryset.filter(**filters)

                paginator = Paginator(queryset, 2)
                page = self.request.GET.get("page")
                rooms = paginator.get_page(page)
                url_parameter = parse.urlencode(parameters, doseq=True)
                context_data["rooms"] = rooms
                context_data["url_parameter"] = url_parameter
        else:
            form = forms.SearchForm()
        context_data["form"] = form
        return context_data




def search(request):
    country = request.GET.get("country")

    if country:
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data["city"]
            country = form.cleaned_data["country"]
            amenities = form.cleaned_data["amenity"]
            instant_book = form.cleaned_data["instant_book"]
            superhost = form.cleaned_data["superhost"]

            queryset = Room.objects.filter()
            filters = {}
            parameters = {}
            if city:
                filters["city__startswith"] = city
                parameters['city'] = city
            if country:
                filters["country"] = country
                parameters['country'] = country

            if amenities:
                for amenity in amenities:
                    queryset = queryset.filter(amenities=amenity)
                    if not parameters.get('amenity'):
                        parameters['amenity'] = []

                    parameters['amenity'].append(amenity.pk)

            queryset = queryset.filter(**filters)

            paginator = Paginator(queryset, 2)
            page = request.GET.get("page")
            rooms = paginator.get_page(page)
            url_parameter = parse.urlencode(parameters, doseq=True)

            return render(
                request,
                "rooms/search.html",
                context={
                    "form": form,
                    "rooms": rooms,
                    "url_parameter": url_parameter
                },
            )
    else:
        form = forms.SearchForm()

    return render(request, "rooms/search.html", context={"form": form})
