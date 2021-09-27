from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.update),
    path('auth/login/', views.login),
]
