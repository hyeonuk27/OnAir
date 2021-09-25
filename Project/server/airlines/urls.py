from django.urls import path
from . import views


urlpatterns = [
    path('profiles/<int:user_pk>/reviews/', views.user_review_list),
    path('logs/', views.user_log_list),
]