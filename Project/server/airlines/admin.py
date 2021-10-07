from django.contrib import admin
from .models import Airline, Arrival, Review, Log, StatisticsResult


admin.site.register(Airline)
admin.site.register(Arrival)
admin.site.register(Review)
admin.site.register(Log)
admin.site.register(StatisticsResult)