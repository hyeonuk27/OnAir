from rest_framework import serializers
from .models import Airline, Arrival, Review, Log, StatisticsResult

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class LogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('user', 'airline', 'arrival')        

class ArrivalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrival
        fields = ('id', 'name', 'image_url')

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('id', 'user', 'airline', 'arrival', 'reg_dt')
        read_only_fields = ('id', 'user', 'airline', 'arrival', 'reg_dt')

class AirlineDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airline
        exclude = ('id',)

class AirlineReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatisticsResult
        fields = ('arrival', 'total', 'under_10', 'under_30', 'over_30', 'delay_rate', 'delay_time')
