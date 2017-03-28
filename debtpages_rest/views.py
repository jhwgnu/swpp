from .models import Debt
from .serializers import DebtSerializer, UserSerializer, UserSumSerializer
from rest_framework import generics
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()

class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSumList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer


class UserSumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer