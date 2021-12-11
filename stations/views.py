from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(row for row in reader)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': data,
        'page': page
    }
    return render(request, 'stations/index.html', context)



