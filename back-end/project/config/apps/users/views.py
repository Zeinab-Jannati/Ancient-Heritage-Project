from django.shortcuts import render
from django.views import generic
from django.cintrib.auth.forms import UserCreationForm
from django.urls import revers_lazy
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = revers_lazy("login")
    template_name = "apps/pages/registretion/register.html"