from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Landing(models.Model):
    title = models.CharField(_("title"), max_length=50)
    detail = models.TextField(_("detail"))
    image = models.ImageField(
        _("image"), upload_to="landings", height_field=None, width_field=None, max_length=None
    )


class Like(models.Model):
    landing = models.ForeignKey(
        Landing, related_name="likes", verbose_name=_("like"), on_delete=models.CASCADE
    )
    ip = models.GenericIPAddressField(_("ip"), protocol="both", unpack_ipv4=False)


class Hate(models.Model):
    landing = models.ForeignKey(Landing, related_name="hates", on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)


class Reservation(models.Model):
    landing = models.ForeignKey(Landing, verbose_name=_("reservation"), on_delete=models.CASCADE)
    email = models.EmailField(_("email"), max_length=254)
    mobile_number = models.CharField(_("mobile_number"), max_length=50)


class Opinion(models.Model):
    email = models.EmailField(_("email"), max_length=254)
    detail = models.TextField(_("detail"))
    mobile_number = models.CharField(_("mobile_number"), max_length=20)
