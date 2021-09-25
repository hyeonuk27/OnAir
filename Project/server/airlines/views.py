from django.shortcuts import get_object_or_404

from .models import Arrival, Review, Log
from accounts.models import User
from .serializers import ReviewListSerializer, LogListSerializer, ArrivalListSerializer

from django.core.paginator import Paginator

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


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
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def user_log_list(request):
    logs = Log.objects.order_by('-reg_dt')
    serializer = LogListSerializer(logs, many=True)
    data = serializer.data
    return Response(data)


# 검색 시 도착지 목록; 로그인 불필요
@api_view(['GET'])
def arrival_list(request):
    arrivals = Arrival.objects.all()
    serializer = ArrivalListSerializer(arrivals, many=True)
    data = serializer.data
    return Response(data)