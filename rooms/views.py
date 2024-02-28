from math import ceil
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage
from .models import Room
from django.views.generic import ListView, DetailView


class ListRooms(ListView):
    model = Room
    paginate_by = 10


class RoomDetail(DetailView):
    model = Room
