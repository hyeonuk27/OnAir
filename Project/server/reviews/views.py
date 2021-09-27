from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required 

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Review
# from .serializers import ReviewListSerializer, ReviewSerializer


@login_required
@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@login_required
@api_view(['GET'])
def review_list(request, airline_id):
    reviews = get_list_or_404(Review, pk=airline_id)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
    

@login_required
@api_view(['DELETE', 'POST'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'DELETE':
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = ReviewSerializer(Review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


api_view(['GET'])
def review_score(request, airline_id):
    score = get_object_or_404(Score)
    serializer = ScoreSerializer(score, many=True)
    return Response(serializer.data)


api_view(['GET'])
def review_keyword(request, airline_id):
    keyword = get_object_or_404(Keyword)
    serializer = KeywordSerializer(keyword, many=True)
    return Response(serializer.data)
