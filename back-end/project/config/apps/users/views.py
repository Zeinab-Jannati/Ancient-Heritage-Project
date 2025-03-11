<<<<<<< HEAD
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
=======
from django.shortcuts import render
from django.views import generic
from django.cintrib.auth.forms import UserCreationForm
from django.urls import revers_lazy
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = revers_lazy("login")
    template_name = "apps/pages/registretion/register.html"
>>>>>>> e3e8f2c550c874fdfc7fb574c29babd19a443117
