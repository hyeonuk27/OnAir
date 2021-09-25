from rest_framework import serializers
from .models import Airline, Arrival, Review, Log, Statistics

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