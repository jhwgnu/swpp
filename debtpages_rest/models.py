from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Debt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    burrower = models.ForeignKey('auth.User', related_name='debts_burrowed', on_delete=models.CASCADE)
    lender = models.ForeignKey('auth.User', related_name='debts_lended', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)