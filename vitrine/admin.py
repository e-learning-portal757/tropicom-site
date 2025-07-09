# C:\Users\DELL\tropicom\tropicom_site\vitrine\admin.py

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Service, ImageSupplementaire, Newsletter, MessageContact, ImageNosRealisation

# Inline pour les images supplémentaires liées à un service
class ImageSupplementaireInline(admin.TabularInline):
    model = ImageSupplementaire
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" style="border:1px solid #ccc; padding:2px;" />')
        return _("Aucune image")
    image_preview.short_description = _("Aperçu")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie')
    search_fields = ('titre', 'categorie', 'description')
    list_filter = ('categorie',)
    inlines = [ImageSupplementaireInline]

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed') # <-- CORRIGÉ ICI
    search_fields = ('email',)
    readonly_fields = ('date_subscribed',)    # <-- CORRIGÉ ICI

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date')
    search_fields = ('nom', 'email', 'sujet', 'message')
    list_filter = ('date',)
    readonly_fields = ('nom', 'email', 'sujet', 'message', 'date')

@admin.register(ImageNosRealisation)
class ImageNosRealisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'image_preview')
    search_fields = ('description',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" style="border:1px solid #ccc; padding:2px;" />')
        return _("Aucune image")
    image_preview.short_description = _("Aperçu")

# Personnalisation des en-têtes du site d'administration
admin.site.site_header = _("Administration Tropicom")
admin.site.site_title = _("Tropicom Admin")
admin.site.index_title = _("Bienvenue dans le tableau de bord")