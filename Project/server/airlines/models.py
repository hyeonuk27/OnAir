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
    is_skyteam = models.BooleanField(null=True, blank=True)
    is_star = models.BooleanField(null=True, blank=True)
    is_oneworld = models.BooleanField(null=True, blank=True)
    total_flight = models.IntegerField()
    total_delayed = models.IntegerField()
    total_canceled = models.IntegerField()


class Arrival(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=50)
    image_url = models.TextField()


class Review(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='reviews')
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


class StatisticsResult(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    # 목적지
    arrival = models.CharField(max_length=50)
    # 항공사
    airline = models.CharField(max_length=20)
    # 목적지에 대한 총운항횟수
    total = models.IntegerField()
    # 10분내 출발확률
    under_10 = models.FloatField()
    # 10분 초과 30분 이하 출발확률
    under_30 = models.FloatField()
    # 30분 초과 출발확률
    over_30 = models.FloatField()
    # 지연률
    delay_rate = models.FloatField()
    # 평균 지연시간
    delay_time = models.IntegerField()
    # 결항률
    cancel_rate = models.FloatField()
    

