from django.contrib import admin
from django.contrib.admin import AdminSite

class TropicomAdminSite(AdminSite):
    site_header = "Administration Tropicom"
    site_title = "Tropicom Admin"
    index_title = "Tableau de bord"

    def each_context(self, request):
        context = super().each_context(request)
        context['css'] = 'css/admin.css'
        return context

admin_site = TropicomAdminSite(name='tropicom_admin')
