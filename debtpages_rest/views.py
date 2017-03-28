from .models import Debt
from .serializers import DebtSerializer, UserSerializer, UserSumSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response

class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSumList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer


class UserSumDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer