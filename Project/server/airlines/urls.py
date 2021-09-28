from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('profiles/<user_id>/reviews/', views.user_review_list),
    path('logs/', views.user_log_list),
    path('arrivals/', views.arrival_list),
    path('airlines/<arrival_id>/', views.airline_list),
    path('reviews/airline/<airline_id>/', views.review_list),
    path('reviews/<review_id>/', views.review_detail),
    path('reviews/score/<airlined_id>/', views.review_score),
    # path('reviews/keword/<airline_id>/', views.review_keyword),
=======
    path('profiles/<int:user_id>/reviews/', views.user_review_list),
    path('logs/', views.user_log_list),
    path('arrivals/', views.arrival_list),
    path('airlines/<arrival_id>/', views.airline_list),
    path('airlines/info/<airline_id>', views.airline_details),
    path('statistics/<arrival_id>/<airline_id>/', views.airline_report)
>>>>>>> 0e5351d3e0369aa5449ab73f723732a081779297
]