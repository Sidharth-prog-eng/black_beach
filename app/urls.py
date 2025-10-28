from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('rooms/',views.rooms, name='rooms'),
    path('attractions/',views.attractions, name='attractions'),
    path('amenities/',views.amenities, name='amenities'),
]