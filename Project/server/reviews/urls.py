from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_create),
    path('<int:airlineId>', views.review_list),
    path('<int:reviewId>', views.review_detail),
    path('score/<int:airlinedId>', views.review_score),
    path('keyword/<int:airlineId>', views.review_keyword),
]