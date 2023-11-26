from django.http import HttpResponse
from django.shortcuts import render


def home(request) -> HttpResponse:
    return HttpResponse("Home page")


def room(request) -> HttpResponse:
    return HttpResponse("Room")
