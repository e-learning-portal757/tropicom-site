from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
# Import du sitemap personnalisé
from .sitemaps import StaticViewSitemap

# Dictionnaire des sitemaps
sitemaps = {
    'static': StaticViewSitemap,
}

# Routes non internationalisées (set_language, sitemap, robots.txt)
urlpatterns = [
    # Pour la sélection de langue
    path('set_language/', set_language, name='set_language'),

    # Sitemap accessible à /sitemap.xml
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # Robots.txt (optionnel pour SEO)
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

# Routes traduites selon la langue active
urlpatterns += i18n_patterns(
   path('admin/', admin.site.urls),

    path('', include('vitrine.urls', namespace='vitrine')),
)


urlpatterns += i18n_patterns(
     path('admin/', admin.site.urls),
    
)
# Fichiers statiques en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
