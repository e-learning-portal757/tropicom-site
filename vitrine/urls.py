from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views


app_name = 'vitrine'

urlpatterns = [
    path('', views.index, name='index'),
    path(_('search/') , views.search_services, name='search_services'),
    path(_('services/'), views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path(_('about/'), views.about, name='about'),
    path(_('contact/'), views.contact, name='contact'),
    path(_('comparatif/'), views.comparatif, name='comparatif'),
    path(_('newsletter/'), views.newsletter, name='newsletter'),
    path('offres-emploi/', views.job_offers_view, name='job_offers'),
]
