from django.urls import path
from . import views


urlpatterns = [
    path('profiles/<user_id>/reviews/', views.user_review_list),
    path('logs/', views.user_log_list),
    path('arrivals/', views.arrival_list),
    path('airlines/<arrival_id>/', views.airline_list),
    path('airlines/<arrival_id>/<airline_id>/', views.airline_report),
    path('airlines/airline/info/<airline_id>/', views.airline_details),
    path('reviews/airline/<airline_id>/', views.review_list),
    path('reviews/<review_id>/', views.review_detail),
    path('reviews/score/<airline_id>/', views.review_score),
    path('reviews/keyword/<airline_id>/', views.review_keyword),
    path('reviews/sentiment/<airline_id>/', views.review_sentiment),
]
