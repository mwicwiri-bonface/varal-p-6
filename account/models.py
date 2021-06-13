from django.db import models


class Payments(models.Model):
    job = models.IntegerField(help_text="micro tasks Id")
    mto = models.IntegerField(help_text="Assigned to MTO")
    payment = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
    fees = models.FloatField()

    class Meta:
        app_label = 'account'


class MTOPaymentStatus(models.Model):
    description = models.CharField(max_length=20, help_text="eg paid, pending")
