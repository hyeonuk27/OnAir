from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Airline(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=20)
    profile_url = models.TextField()
    address = models.TextField()
    phone_number = models.TextField()
    site_url = models.TextField()
    corona_url = models.TextField()
    is_skypass = models.BooleanField(null=True, blank=True)
    is_star = models.BooleanField(null=True, blank=True)
    is_oneworld = models.BooleanField(null=True, blank=True)


class Arrival(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=50)
    image_url = models.TextField()


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


class Log(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    reg_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='logs')
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, related_name='logs')


class Statistics(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    date = models.DateTimeField()
    airline = models.CharField(max_length=20)
    arrival = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    reason = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.IntegerField()
    delayed_time = models.IntegerField()