from django.urls import path
from . import views


urlpatterns = [
    path('profiles/<int:user_id>/reviews/', views.user_review_list),
    path('logs/', views.user_log_list),
    path('arrivals/', views.arrival_list),
    path('airlines/<arrival_id>/', views.airline_list),
    path('airlines/info/<airline_id>', views.views.airline_details),
    path('statistics/<arrival_id>/<airline_id>/', views.airline_report)
]