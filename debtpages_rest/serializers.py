from rest_framework import serializers
from .models import Debt
from django.contrib.auth.models import User

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id','created','amount','burrower','lender')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')