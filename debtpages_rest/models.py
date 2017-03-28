from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User
from django.conf import settings

class Debt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    borrower = models.ForeignKey('auth.User', related_name='debts_as_borrower', on_delete=models.CASCADE)
    lender = models.ForeignKey('auth.User', related_name='debts_as_lender', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
