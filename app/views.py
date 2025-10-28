from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def rooms(request):
    return render(request, 'rooms.html')
def amenities(request):
    return render(request, 'amenities.html')
def attractions(request):
    return render(request, 'attractions.html')


