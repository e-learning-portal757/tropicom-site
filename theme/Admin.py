from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import CategorieService, Service, MessageContact, InformationsSite

@admin.register(CategorieService)
class CategorieServiceAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
    verbose_name = _("Catégorie de service")
    verbose_name_plural = _("Catégories de services")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie')
    search_fields = ('titre', 'description')
    list_filter = ('categorie',)
    verbose_name = _("Service")
    verbose_name_plural = _("Services")

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoye')
    search_fields = ('nom', 'email', 'sujet', 'message')
    readonly_fields = ('nom', 'email', 'sujet', 'message', 'date_envoye')
    ordering = ('-date_envoye',)
    verbose_name = _("Message de contact")
    verbose_name_plural = _("Messages de contact")

@admin.register(InformationsSite)
class InformationsSiteAdmin(admin.ModelAdmin):
    list_display = ('nom_entreprise', 'email', 'telephone')
    search_fields = ('nom_entreprise', 'email')
    verbose_name = _("Informations du site")
    verbose_name_plural = _("Informations du site")
