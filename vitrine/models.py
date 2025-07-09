# C:\Users\DELL\tropicom\tropicom_site\vitrine\models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    titre = models.CharField(_("Titre"), max_length=255)
    image = models.ImageField(_("Image"), upload_to='services/')
    description = models.TextField(_("Description"))
    categorie = models.CharField(_("Catégorie"), max_length=100, default="Général")
    prestations = models.TextField(
        _("Prestations"),
        help_text=_("Sépare chaque prestation par un point-virgule (;)"),
        default=_("Aucune prestation")
    )

    def __str__(self):
        return self.titre

    def get_prestations(self):
        return self.prestations.split(';')

    def as_dict(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'image': self.image.url,
            'description': self.description,
        }

class ImageSupplementaire(models.Model):
    service = models.ForeignKey('Service', related_name='images_supplementaires', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='services/supplementaires/')
    description = models.TextField(_("Description"), blank=True)

    def __str__(self):
        return f"{_('Image de')} {self.service.titre}"

# AJOUTEZ CE MODÈLE ICI
class Newsletter(models.Model):
    email = models.EmailField(_("Email"), unique=True)
    date_subscribed = models.DateTimeField(_("Date d'abonnement"), auto_now_add=True)

    class Meta:
        verbose_name = _("Abonné à la newsletter")
        verbose_name_plural = _("Abonnés à la newsletter")

    def __str__(self):
        return self.email

class MessageContact(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)
    email = models.EmailField(_("Email"))
    sujet = models.CharField(_("Sujet"), max_length=200)
    message = models.TextField(_("Message"))
    date = models.DateTimeField(_("Date"), auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

# Vous avez une deuxième `from django.db import models` ici, c'est redondant.
# Supprimez cette ligne ou assurez-vous qu'elle n'est pas nécessaire.
# from django.db import models # <-- CELLE-CI !

class ImageNosRealisation(models.Model):
    titre = models.CharField(max_length=255, default=_("Image sans titre")) # Ajout de _() pour la traduction
    image = models.ImageField(upload_to='realisations/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titre