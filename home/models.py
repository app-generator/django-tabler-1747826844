# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    ean = models.TextField(max_length=255, null=True, blank=True)
    mb = models.TextField(max_length=255, null=True, blank=True)
    brand = models.TextField(max_length=255, null=True, blank=True)
    product_name = models.TextField(max_length=255, null=True, blank=True)
    fv = models.IntegerField(null=True, blank=True)
    prezzo_retailer = models.IntegerField(null=True, blank=True)
    ean_retailer = models.TextField(max_length=255, null=True, blank=True)
    netto_fattura = models.IntegerField(null=True, blank=True)
    product_name_ahe = models.TextField(max_length=255, null=True, blank=True)
    ean13_ahe = models.TextField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")



#__MODELS__END
