from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Service, Newsletter, ImageNosRealisation, MessageContact

def index(request):
    services = Service.objects.all()
    images_nos_realisations = ImageNosRealisation.objects.all()
    return render(request, 'vitrine/index.html', {
        'services': services,
        'images_nos_realisations': images_nos_realisations
    })


def search_services(request):
    """
    Recherche simple dans les services.
    """
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        query_lower = query.lower()
        results = Service.objects.filter(
            titre__icontains=query_lower
        ) | Service.objects.filter(
            description__icontains=query_lower
        )
    return render(request, 'vitrine/search_results.html', {
        'query': query,
        'results': results,
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'vitrine/services.html', {'services': services})

def about(request):
    return render(request, 'vitrine/about.html')

def comparatif(request):
    return render(request, 'vitrine/comparatif.html')

def contact(request):
    """
    Affiche ou traite le formulaire de contact.
    """
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email_expediteur = request.POST.get('email') # Renommé pour plus de clarté
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        if nom and email_expediteur and sujet and message: # Utilisation de email_expediteur
            # Enregistre le message dans l'admin
            try:
                MessageContact.objects.create(
                    nom=nom,
                    email=email_expediteur, # Utilisation de email_expediteur
                    sujet=sujet,
                    message=message
                )
                messages.success(request, _("Votre message a été envoyé avec succès."))
            except Exception as e:
                messages.error(request, _("Erreur lors de l'enregistrement du message : ") + str(e))
                print(f"Erreur d'enregistrement du message : {e}")
                # Si l'enregistrement échoue, on peut choisir de ne pas envoyer l'email non plus
                return redirect('vitrine:contact') # Redirige ici si l'enregistrement échoue

            # Envoi de l'email
            try:
                send_mail(
                    subject=_("[Contact] ") + f"{sujet} - {nom}",
                    message=_("Message de ") + f"{nom} ({email_expediteur}):\n\n{message}", # Utilisation de email_expediteur
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    # MODIFICATION ICI : Ciblez les adresses e-mail définies dans settings.ADMINS
                    recipient_list=[admin_email for name, admin_email in settings.ADMINS], 
                    fail_silently=False,
                )
                # Le message de succès est déjà géré par l'enregistrement ci-dessus
            except Exception as e:
                messages.error(request, _("Erreur lors de l'envoi de l'email à l'administrateur : ") + str(e))
                print(f"Erreur d'envoi d'e-mail: {e}")
        else:
            messages.error(request, _("Tous les champs sont requis."))

        return redirect('vitrine:contact')

    return render(request, 'vitrine/contact.html')


def newsletter(request):
    """
    Enregistrement d'un email à la newsletter.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email)
                messages.success(request, _("Merci pour votre inscription à la newsletter."))
            else:
                messages.info(request, _("Cet email est déjà inscrit."))
        else:
            messages.error(request, _("Veuillez entrer une adresse email valide."))
    return redirect('index')

def services_view(request):
    services = Service.objects.prefetch_related('images_supplementaires').all()

    services_json = json.dumps([
        {
            "id": service.id,
            "titre": service.titre,
            "description": service.description,
            "image": service.image.url,
            "images_supplementaires": [
                {
                    "url": img.image.url,
                    "description": img.description
                } for img in service.images_supplementaires.all()
            ]
        } for service in services
    ], cls=DjangoJSONEncoder)

    return render(request, 'services.html', {
        'services': services,
        'services_json': services_json,
    })
