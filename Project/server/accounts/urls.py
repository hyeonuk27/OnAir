from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('auth/login/', views.google_login),
    path('api-token-auth/', obtain_jwt_token),
]
