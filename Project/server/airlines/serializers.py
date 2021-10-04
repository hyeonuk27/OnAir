from rest_framework import serializers
from .models import Airline, Arrival, Review, Log, StatisticsResult

class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    userid = serializers.ReadOnlyField()
    userpic = serializers.ReadOnlyField()
    arrivalname = serializers.ReadOnlyField()


    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = '__all__'


class LogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = '__all__'       

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
        fields = '__all__'

class AirlineReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatisticsResult
        fields = ('arrival', 'total', 'under_30', 'under_60', 'over_60', 'delay_rate', 'delay_time')


