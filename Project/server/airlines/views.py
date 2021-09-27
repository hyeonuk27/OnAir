from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Airline, Arrival, Review, Log, StatisticsResult
from accounts.models import User
from .serializers import AirlineDetailSerializer, AirlineReportSerializer, ReviewListSerializer, LogListSerializer, ArrivalListSerializer, LogSerializer

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

import json
import pandas as pd
import numpy as np
import joblib
from decouple import config

import requests
import json

from datetime import datetime


# id 생성
def make_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(13))


# 머신러닝 원핫인코딩 인코더
def get_encoded(data,labelencoder_dict,onehotencoder_dict):
    # except passengers
    data_exc = data.iloc[:, :-1]
    encoded_x = None
    for i in range(0,data_exc.shape[1]):
        label_encoder =  labelencoder_dict[i]
        feature = label_encoder.transform(data_exc.iloc[:,i])
        feature = feature.reshape(data_exc.shape[0], 1)
        onehot_encoder = onehotencoder_dict[i]
        feature = onehot_encoder.transform(feature)
        if encoded_x is None:
            encoded_x = feature
        else:
            encoded_x = np.concatenate((encoded_x, feature), axis=1)

    encoded_x = np.concatenate((encoded_x, data.iloc[:, -1].to_numpy().reshape(-1, 1)), axis=1)

    return encoded_x


# 유저가 작성한 리뷰 리스트 + 계정 정보
# 로그인 불필요
@api_view(['GET'])
def user_review_list(request, user_id):
    user_reviews = Review.objects.filter(user_id=request.user.id).order_by('-created_at')
    user_profile = get_object_or_404(User, pk=user_id)
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
        logs = Log.objects.filter(user_id=request.user.id).order_by('-reg_dt')[:10]
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
    arrivals = get_list_or_404(Arrival)
    serializer = ArrivalListSerializer(arrivals, many=True)
    data = serializer.data
    return Response(data)


# 검색 시 항공사 리스트
@api_view(['GET'])
def airline_list(request, arrival_id):
    arrival = get_object_or_404(Arrival, pk=arrival_id)
    # 직접 JSON 형태의 데이터를 만들어서 반환
    response_data = {'Airlines': []}
    airlines = get_list_or_404(Airline)
    # 머신러닝 모델 및 인코더, 스케일러 로딩
    model = joblib.load('predict_models/ml_delay/delay_rate_predict.pkl')
    labelencoder = joblib.load('predict_models/ml_delay/labelencoder_dict.pkl')
    onehotencoder = joblib.load('predict_models/ml_delay/onehotencoder_dict.pkl')
    scaler = joblib.load('predict_models/ml_delay/passengers_min_max_scaler.pkl')
    # Openweathermap API로 인천 공항의 현재 날씨 받아오기
    URL = 'https://api.openweathermap.org/data/2.5/weather?lat=37.46&lon=126.44&appid=%s' % config('WEATHER_API_KEY')
    weather = requests.get(url=URL).json().get('weather')[0].get('main')
    for airline in airlines:
        # 목적지, 항공사에 해당하는 통계 결과 가져오기
        statistics_result = StatisticsResult.objects.filter(airline=airline.name, arrival=arrival.name).first()
        # 목적지, 항공사에 해당하는 이번달 이용객수 예측값 가져오기
        df = pd.read_csv('predict_models/ets_passengers/predict_data/%s.csv' % airline.name)
        predicted_data = df[df['date'].str.startswith('%s' % datetime.today().strftime("%Y-%m"))]['passengers'][0]
        scaled_passengers = scaler.transform(pd.DataFrame([[predicted_data]]))
        # 머신러닝 모델 가져와서 오늘 날씨, 이번달 이용객수의 지연률 예측
        data = pd.DataFrame([[airline.name, arrival.name, weather, scaled_passengers]], columns = ['airline', 'arrival', 'weather', 'passengers'])
        input_data = get_encoded(data, labelencoder, onehotencoder)
        response_data.get('Airlines').append(
            {
                'id': airline.id,
                'name': airline.name,
                'profile_url': airline.profile_url,
                'total': statistics_result.total,
                'delay_rate': statistics_result.delay_rate,
                'delay_time': statistics_result.delay_time,
                'predicted_delay_rate': round(model.predict_proba(input_data)[0, 1] * 100, 2)
            }
        )
    
    # Python의 dictionary를 Json형태로 반환하기 위함
    return HttpResponse(json.dumps(response_data), content_type = 'application/javascript; charset=utf8')

@api_view(['GET'])
def airline_report(request, arrival_id, airline_id):
    # airline = get_object_or_404(Airline, pk=airline_id)
    # arrival = get_object_or_404(Arrival, pk=arrival_id)
    # statistics_result = StatisticsResult.objects.filter(airline=airline.name, arrival=arrival.name).first()
    # airline, arrival 넣으면 통계 데이터를 가져오는 함수를 만들어야 하는데 아직 csv 파일 완성이 안되어서 이 부분만 시간이 좀 더 걸릴 것 같음
    pass



# 로그인 불필요
@api_view(['GET'])
def airline_details(request, airline_id):
    airline = get_object_or_404(Airline, pk=airline_id)
    serializer = AirlineDetailSerializer(airline)
    data = serializer.data
    return Response(data)