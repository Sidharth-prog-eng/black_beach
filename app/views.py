from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'is_homepage': True})

def about(request):
    return render(request, 'about.html', {'is_homepage': False})

def contact(request):
    return render(request, 'contact.html', {'is_homepage': False})

def rooms(request):
    return render(request, 'rooms.html', {'is_homepage': False})

def amenities(request):
    return render(request, 'amenities.html', {'is_homepage': False})

def attractions(request):
    return render(request, 'attractions.html', {'is_homepage': False})


