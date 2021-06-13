from django.db import models

from user.models import CustomUser


class Mto(CustomUser):
    paypal_id = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'MTO'
        verbose_name_plural = 'MTO'
