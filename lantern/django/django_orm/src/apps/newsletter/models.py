from django.db import models
from common.models import BaseDateAuditModel
from django.utils.translation import gettext_lazy as _


class NewsLetter(BaseDateAuditModel):
    email = models.EmailField()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.email