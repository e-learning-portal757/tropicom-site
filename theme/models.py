from django.db import models
from django.utils.translation import gettext_lazy as _

# Catégories de services (ex: Réseaux, Sécurité...)
class CategorieService(models.Model):
    nom = models.CharField(_("Nom de la catégorie"), max_length=100)

    class Meta:
        verbose_name = _("Catégorie de service")
        verbose_name_plural = _("Catégories de services")

    def __str__(self):
        return self.nom

# Services (liés à une catégorie)
class Service(models.Model):
    titre = models.CharField(_("Titre"), max_length=100)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to='services/')
    categorie = models.ForeignKey(CategorieService, on_delete=models.CASCADE, verbose_name=_("Catégorie"))

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.titre

# Messages de contact
class MessageContact(models.Model):
    nom = models.CharField(_("Nom"), max_length=100)
    email = models.EmailField(_("Email"))
    sujet = models.CharField(_("Sujet"), max_length=150)
    message = models.TextField(_("Message"))
    date_envoye = models.DateTimeField(_("Date d'envoi"), auto_now_add=True)

    class Meta:
        verbose_name = _("Message de contact")
        verbose_name_plural = _("Messages de contact")

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

# Informations du site (à propos, contact, etc.)
class InformationsSite(models.Model):
    nom_entreprise = models.CharField(_("Nom de l'entreprise"), max_length=100)
    email = models.EmailField(_("Email"))
    telephone = models.CharField(_("Téléphone"), max_length=20)
    adresse = models.TextField(_("Adresse"))
    a_propos = models.TextField(_("À propos"))

    class Meta:
        verbose_name = _("Informations du site")
        verbose_name_plural = _("Informations du site")

    def __str__(self):
        return self.nom_entreprise
