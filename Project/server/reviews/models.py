from django.db import models
from django.conf import settings
from airlines.models import Airline, Arrival

User = settings.AUTH_USER_MODEL

class Review(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='reviews')
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, related_name='reviews')
    title = models.TextField()
    content = models.TextField()
    flight_at = models.DateField()
    seat = models.CharField(max_length=10)
    score = models.IntegerField()
    seat_score = models.IntegerField(null=True, blank=True)
    service_score = models.IntegerField(null=True, blank=True)
    checkin_score = models.IntegerField(null=True, blank=True)
    food_score = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)