from django.contrib.auth.models import User

from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',)),
        ]

        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=20, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=20, null=True, blank=False)
    email = models.CharField(max_length=20, null=True, blank=False)

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')

        indexes = [
            Index(fields=['user', ])
        ]

    @property
    def title(self):
        return f'{self.get_full_name()}, from: {self.city.name}, email: {self.email}'

    def __str__(self):
        return self.user.username
