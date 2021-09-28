from rest_framework import serializers
from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = ('id', 'title', )


# detail
class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = '__all__'