from django.urls import path
from . import views


urlpatterns = [
    path('profiles/<user_id>/reviews/', views.user_review_list),
    path('logs/', views.user_log_list),
    path('arrivals/', views.arrival_list),
    path('airlines/<arrival_id>/', views.airline_list),
    path('reviews/', views.review_create),
    path('reviews/<airline_id>', views.review_list),
    path('reviews/<int:review_id>', views.review_detail),
    path('reviews/score/<airline_id>', views.review_score),
    path('reviews/keword/<airline_id>/', views.review_keyword),
]