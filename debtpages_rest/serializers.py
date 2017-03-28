from rest_framework import serializers
from debtpages_rest.models import Debt


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'amount')