from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Airline(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=20)
    profile_url = models.TextField()
    address = models.TextField()
    detail = models.TextField()
    phone_number = models.TextField()
    site_url = models.TextField()
    corona_url = models.TextField()
    is_skyteam = models.BooleanField(null=True, blank=True)
    is_star = models.BooleanField(null=True, blank=True)
    is_oneworld = models.BooleanField(null=True, blank=True)
    total_flight = models.IntegerField()
    total_delayed = models.IntegerField()
    total_canceled = models.IntegerField()
    under_30 = models.IntegerField()
    under_60 = models.IntegerField()
    over_60 = models.IntegerField()
    
    def __str__(self):
        return self.name


class Arrival(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=50)
    # image_url = models.TextField()
    
    def __str__(self):
        return self.name


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

    def username(self):
        return self.user.name

    def userid(self):
        return self.user.id

    def userpic(self):
        return self.user.profile_url

    def arrivalname(self):
        return self.arrival.name

    def __str__(self):
        return self.title


class Log(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    reg_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='logs')
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, related_name='logs')


class StatisticsResult(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    arrival = models.CharField(max_length=50)
    airline = models.CharField(max_length=20)
    total = models.IntegerField()
    under_30 = models.FloatField()
    under_60 = models.FloatField()
    over_60 = models.FloatField()
    delay_rate = models.FloatField()
    delay_time = models.IntegerField()
    cancel_rate = models.FloatField()

    def __str__(self):
        return self.arrival, self.airline