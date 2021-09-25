from rest_framework import serializers
from .models import Review, Log

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class LogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('user', 'airline', 'arrival')        