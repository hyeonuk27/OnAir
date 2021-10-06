from django.contrib import admin
from .models import Airline, Arrival, Review, Log, StatisticsResult

# Register your models here.

admin.site.register(Airline)
admin.site.register(Arrival)
admin.site.register(Review)
admin.site.register(Log)
admin.site.register(StatisticsResult)