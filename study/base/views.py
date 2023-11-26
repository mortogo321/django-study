from django.shortcuts import render


def home(request) -> render:
    return render(request, "base/home.html")


def room(request) -> render:
    return render(request, "base/room.html")
