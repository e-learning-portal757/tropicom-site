from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q # Ajouté pour search_services

# Importez tous vos modèles nécessaires ici.
# J'ai REMPLACÉ 'ServiceImage' par un commentaire.
# Si vous avez un modèle pour les images supplémentaires, mettez son nom réel ici.
from .models import Service, Newsletter, ImageNosRealisation, MessageContact, JobOffer 
# Exemple: from .models import Service, Newsletter, ImageNosRealisation, MessageContact, JobOffer, VotreModelePourImagesSupplementaires


def index(request):
    services = Service.objects.all()
    images_nos_realisations = ImageNosRealisation.objects.all()
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/index.html', {
        'services': services,
        'images_nos_realisations': images_nos_realisations,
        'has_active_job_offers': has_active_job_offers,
    })


def search_services(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        results = Service.objects.filter(
            Q(titre__icontains=query) | Q(description__icontains=query)
        )
    
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/search_results.html', {
        'query': query,
        'results': results,
        'has_active_job_offers': has_active_job_offers,
    })

def services(request):
    services = Service.objects.all()
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/services.html', {
        'services': services,
        'has_active_job_offers': has_active_job_offers,
    })

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()

    context = {
        'service': service,
        'has_active_job_offers': has_active_job_offers,
    }
    return render(request, 'vitrine/service_detail.html', context)


def about(request):
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/about.html', {
        'has_active_job_offers': has_active_job_offers,
    })

def comparatif(request):
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/comparatif.html', {
        'has_active_job_offers': has_active_job_offers,
    })

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email_expediteur = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        if nom and email_expediteur and sujet and message:
            try:
                MessageContact.objects.create(
                    nom=nom,
                    email=email_expediteur,
                    sujet=sujet,
                    message=message
                )
                messages.success(request, _("Votre message a été envoyé avec succès."))
            except Exception as e:
                messages.error(request, _("Erreur lors de l'enregistrement du message : ") + str(e))
                print(f"Erreur d'enregistrement du message : {e}")
                return redirect('vitrine:contact')

            try:
                send_mail(
                    subject=_("[Contact] ") + f"{sujet} - {nom}",
                    message=_("Message de ") + f"{nom} ({email_expediteur}):\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[admin_email for name, admin_email in settings.ADMINS], 
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, _("Erreur lors de l'envoi de l'email à l'administrateur : ") + str(e))
                print(f"Erreur d'envoi d'e-mail: {e}")
        else:
            messages.error(request, _("Tous les champs sont requis."))

        return redirect('vitrine:contact')

    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/contact.html', {
        'has_active_job_offers': has_active_job_offers,
    })


def newsletter(request):
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
    return redirect('vitrine:index') 

def services_view(request):
    services = Service.objects.prefetch_related('images_supplementaires').all()

    services_json = json.dumps([
        {
            "id": service.id,
            "titre": service.titre,
            "description": service.description,
            "image": service.image.url if service.image else None,
            "images_supplementaires": [
                {
                    "url": img.image.url,
                    "description": img.description
                } for img in service.images_supplementaires.all()
            ] if hasattr(service, 'images_supplementaires') else [] # Ajout d'une vérification hasattr
        } for service in services
    ], cls=DjangoJSONEncoder)

    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return render(request, 'vitrine/services.html', {
        'services': services,
        'services_json': services_json,
        'has_active_job_offers': has_active_job_offers,
    })
    
def job_offers_view(request):
    active_job_offers = JobOffer.objects.filter(is_active=True).order_by('-created_at')
    has_active_job_offers = active_job_offers.exists()
    return render(request, 'vitrine/job_offers.html', {
        'job_offers': active_job_offers,
        'has_active_job_offers': has_active_job_offers,
    })
    
def faq(request):
    """
    Vue pour la page FAQ.
    """
    return render(request, 'vitrine/faq.html', {})