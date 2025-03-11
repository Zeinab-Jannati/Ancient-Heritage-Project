from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

urlpatterns= [
    path("register/" ,views.RegisterView.as_view() , name="register")
]