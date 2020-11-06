from django.db import models

# Create your models here.


class PhoneModel(models.Model):
    mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return str(self.mobile)
