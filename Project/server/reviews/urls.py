from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_create),
    path('<int:airline_id>', views.review_list),
    path('<int:review_id>', views.review_detail),
    path('score/<int:airlined_id>', views.review_score),
    path('keyword/<int:airline_id>', views.review_keyword),
]