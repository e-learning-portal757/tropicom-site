from django.urls import path
from . import views

app_name = 'vitrine'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_services, name='search_services'),  # <-- ici la vue + le nom
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
