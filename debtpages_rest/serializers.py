from rest_framework import serializers
from .models import Debt
from django.contrib.auth.models import User
from django.db.models import Sum

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id','created','amount','borrower','lender')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','debts_as_borrower','debts_as_lender')


class UserSumSerializer(serializers.ModelSerializer):
    lended_money = serializers.SerializerMethodField('func1')
    borrowed_money = serializers.SerializerMethodField('func2')

    def func1(self, user):
        return user.debts_as_lender.aggregate(sum=Sum('amount'))['sum']

    def func2(self, user):
        return user.debts_as_borrower.aggregate(sum=Sum('amount'))['sum']

    class Meta:
        model = User
        fields = ('id','username','lended_money','borrowed_money')