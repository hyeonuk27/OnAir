from django.shortcuts import get_object_or_404

from .models import Airline, Arrival, Review, Log
from accounts.models import User
from .serializers import ReviewListSerializer, LogListSerializer, ArrivalListSerializer, LogSerializer

from django.core.paginator import Paginator

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status

from airlines import serializers

import string
import random
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


def make_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(13))


# 유저가 작성한 리뷰 리스트 + 계정 정보
# 로그인 불필요
@api_view(['GET'])
def user_review_list(request, user_pk):
    user_reviews = Review.objects.filter(user_pk=request.user.id).order_by('-created_at')
    user_profile = get_object_or_404(User, pk=user_pk)
    page = request.GET.get('page', '1')
    paginator = Paginator(user_reviews, 5)
    user_reviews = paginator.get_page(page)
    serializer = ReviewListSerializer(user_reviews, many=True)
    data = serializer.data
    data.append({'user_profile': user_profile})
    return Response(data)


# 로그인 필요
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'airline_id': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
            'arrival_id': openapi.Schema(type=openapi.TYPE_STRING, description='The desc'),
        }))
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def user_log_list(request):
    if request.method == 'GET':
        logs = Log.objects.order_by('-reg_dt')
        serializer = LogListSerializer(logs, many=True)
        data = serializer.data
        return Response(data)
    elif request.method == 'POST':
        airline = get_object_or_404(Airline, pk=request.data.get('airline_id'))
        arrival = get_object_or_404(Arrival, pk=request.data.get('arrival_id'))
        while True:
            id = make_random_id()
            if(Log.objects.filter(id=id).exists()):
                continue
            else:
                break
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(id=id, user=request.user, airline=airline, arrival=arrival)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 검색 시 도착지 목록; 로그인 불필요
@api_view(['GET'])
def arrival_list(request):
    arrivals = Arrival.objects.all()
    serializer = ArrivalListSerializer(arrivals, many=True)
    data = serializer.data
    return Response(data)


# 통계 자료 조회
@api_view(['GET'])
def airline_detail(request, arrival_id, airline_id):
    airline = get_object_or_404(Airline, pk=airline_id)
    arrival = get_object_or_404(Arrival, pk=arrival_id)
    serializer = Airline


# 항공사 정보 조회