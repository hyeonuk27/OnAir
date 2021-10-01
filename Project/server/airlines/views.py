from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Avg
from django.http import HttpResponse

from .models import Airline, Arrival, Review, Log, StatisticsResult
from accounts.models import User
from .models import Review
from .serializers import AirlineDetailSerializer, AirlineReportSerializer, ReviewListSerializer, ReviewSerializer, LogListSerializer, ArrivalListSerializer, LogSerializer
from accounts.utils import check_login

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
import jwt

import time
# import datetime as dt
from datetime import datetime
from collections import Counter
from eunjeon import Mecab

JWT_SECRET_KEY = config('JWT_SECRET_KEY')

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


# 머신러닝 원핫인코딩 인코더 - 목적지, 항공사, 날씨로만 예측용
def get_encoded_weather(data,labelencoder_dict,onehotencoder_dict):
    # except passengers
    data_exc = data
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
        if statistics_result == None:
            continue
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
    return HttpResponse(json.dumps(response_data), content_type = 'application/json; charset=utf8')

@api_view(['GET'])
def airline_report(request, arrival_id, airline_id):
    airline = get_object_or_404(Airline, pk=airline_id)
    arrival = get_object_or_404(Arrival, pk=arrival_id)
    statistics_result = StatisticsResult.objects.filter(airline=airline.name, arrival=arrival.name).first()
    
    labelencoder = joblib.load('predict_models/ml_delay/labelencoder_dict.pkl')
    onehotencoder = joblib.load('predict_models/ml_delay/onehotencoder_dict.pkl')
    scaler = joblib.load('predict_models/ml_delay/passengers_min_max_scaler.pkl')
    
    # 오늘 날씨, 이번달 이용객수에 따른 예측값은 항공사 리스트로부터 router.push의 파라미터로 받는다.
    # 날씨에 따른 지연률 예측값 리스트
    weather_model = joblib.load('predict_models/ml_delay/delay_rate_weather_predict.pkl')
    weather_list = ['Clear', 'Clouds', 'Mist', 'Haze', 'Rain', 'Fog', 'Snow', 'Dust', 'Drizzle', 'Thunderstorm', 'Typhoon', 'Smoke']
    predicted_by_weather = []
    for weather in weather_list:
        df = pd.DataFrame([[airline.name, arrival.name, weather]], columns = ['airline', 'arrival', 'weather'])
        input_data = get_encoded_weather(df, labelencoder, onehotencoder)
        predicted_by_weather.append(round(weather_model.predict_proba(input_data)[0, 1] * 100, 2))
    
    # 월별 이용객수에 따른 향후 3개월 지연률 예측값 리스트
    passengers_model = joblib.load('predict_models/ml_delay/delay_rate_passengers_predict.pkl')
    month = datetime.today().month
    month_list = [
        '%d월' % month, 
        '%d월' % (month + 1) if (month + 1) < 13 else (month + 1 - 12), 
        '%d월' % (month + 2) if (month + 2) < 13 else (month + 2 - 12)
    ]
    # 이번달부터 3개월 이용객수 예측 파일 로드
    predicted_data = pd.read_csv('predict_models/ets_passengers/predict_data/%s.csv' % airline.name)
    predicted_by_passengers = []
    # 1개월마다 지연률 예측값 구하기
    for i in range(3):
        scaled_passengers = scaler.transform(pd.DataFrame([[predicted_data['passengers'].values[i]]]))
        df = pd.DataFrame([[airline.name, arrival.name, scaled_passengers]], columns = ['airline', 'arrival', 'passengers'])
        input_data = get_encoded(df, labelencoder, onehotencoder)
        predicted_by_passengers.append(round(passengers_model.predict_proba(input_data)[0, 1] * 100, 2))
    
    # 통계

    # 항공사 필터
    airlinedata = pd.read_csv('statistics/preprocessing/statistics_data.csv')
    airline_filter = airlinedata[airlinedata['airline'] != f'{airline.name}'].index
    airlinedata = airlinedata.drop(airline_filter)

    # 지연 필터
    d_filter = airlinedata[airlinedata['state'] != '지연'].index
    reason_group = airlinedata.drop(d_filter).reset_index(drop=True)

    # 목적지 필터
    arrival_filter = reason_group[reason_group['arrival'] != f'{arrival.name}'].index
    reason_group = reason_group.drop(arrival_filter).reset_index(drop=True)
    reason_group = reason_group.drop(columns=['date', 'arrival', 'passengers', 'state'])

    # 지연사유 개수
    reason_count = reason_group.groupby('reason').count().reset_index()
    reason_count = reason_count.drop(columns=['delayed_time'])
    reason_count.rename(columns = {'airline' : 'total'}, inplace = True)

    # 지연사유별 평균지연시간
    reason_avg = reason_group.groupby(by=['reason'], as_index=False).mean().reset_index()
    reason_avg.rename(columns = {'airline' : 'avg_time'}, inplace = True)
    reason_avg['delayed_time'] = round(reason_avg['delayed_time'], 2)

    # 지연사유별 개수와 평균지연시간
    merge_chart = pd.merge(reason_count, reason_avg, on="reason", how='left')
    
    reason_list = merge_chart['reason'].values.tolist()
    reason_cnt_list = merge_chart['total'].values.tolist()
    avg_delayed_time_list = merge_chart['delayed_time'].values.tolist()

    # 월별 이용객 시계열
    monthly = pd.read_csv(f'predict_models/ets_passengers/{airline.name}.csv')
    dates_list = monthly['date'].values.tolist()
    # print(dates_list)
    dates_list = list(map(lambda x: int((time.mktime(datetime.strptime(x, "%Y-%m-%d").timetuple()) + 32400) * 1000), dates_list))
    passengers_cnt = monthly['passengers'].values.tolist()

    # int((time.mktime(datetime.datetime.strptime(a, "%Y-%m-%d").timetuple()) + 32400) * 1000)

    monthly_data = list()
    for i in range(len(dates_list)):
        monthly_data.append([dates_list[i], passengers_cnt[i]])

    response_data = {
        'data': {
            'airline_id': airline.id,
            'airline_name': airline.name,
            'airline_profile_url': airline.profile_url,
            'airline_address': airline.address,
            'airline_phone_number': airline.phone_number,
            'airline_site_url': airline.site_url,
            'airline_corona_url': airline.corona_url,
            'airline_is_skyteam': airline.is_skyteam,
            'airline_is_star': airline.is_star,
            'airline_is_oneworld': airline.is_oneworld,
            'arrival_id': arrival.id,
            'arrival_name': arrival.name,
            'arrival_image_url': arrival.image_url,
            'total': statistics_result.total,
            'under_30': statistics_result.under_30,
            'under_60': statistics_result.under_60,
            'over_60': statistics_result.over_60,
            'delay_rate': statistics_result.delay_rate,
            'delay_time': statistics_result.delay_time,
            'airline_arrival_delay_reason_list': reason_list,
            'airline_arrival_delay_reason_count_list': reason_cnt_list,
            'airline_arrival_avg_delayed_time_by_reason_list': avg_delayed_time_list,
            'weather_list': weather_list,
            'predicted_by_weather': predicted_by_weather,
            'month_list': month_list,
            'predicted_by_passengers': predicted_by_passengers,
            'passengers_by_month': monthly_data,
        }   
    }

    return HttpResponse(json.dumps(response_data), content_type = 'application/json; charset=utf8')


# 로그인 불필요
@api_view(['GET'])
def airline_details(request, airline_id):
    airline = get_object_or_404(Airline, pk=airline_id)
    serializer = AirlineDetailSerializer(airline)
    data = serializer.data
    return Response(data)
    

@api_view(['POST', 'GET'])
def review_list(request, airline_id):
    if request.method == 'POST':
        jwt_token = request.headers["Authorization"]
        user_id = jwt.decode(jwt_token, JWT_SECRET_KEY, algorithm='HS256')
        user = get_object_or_404(User, id=user_id['id'])
        while True:
            review_id = make_random_id()
            if(Review.objects.filter(id=review_id).exists()):
                continue
            else:
                break
        airline = get_object_or_404(Airline, id=airline_id)
        review = Review(id=review_id)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(airline=airline, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        reviews = get_list_or_404(Review, airline=airline_id)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    

@api_view(['DELETE', 'PUT'])
@check_login
def review_detail(request, review_id):
    print('test')
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user:
        if request.method == 'DELETE':
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


@api_view(['GET'])
def review_score(request, airline_id):
    score = Review.objects.filter(airline=airline_id).aggregate(Avg('score'))
    seat_score = Review.objects.filter(airline=airline_id, seat_score__isnull=False).aggregate(Avg('seat_score'))
    service_score = Review.objects.filter(airline=airline_id, service_score__isnull=False).aggregate(Avg('service_score'))
    checkin_score = Review.objects.filter(airline=airline_id, checkin_score__isnull=False).aggregate(Avg('checkin_score'))
    food_score = Review.objects.filter(airline=airline_id, food_score__isnull=False).aggregate(Avg('food_score'))
    
    review_score = {
        'score': score['score__avg'],
        'seat_score': seat_score['seat_score__avg'],
        'service_score': service_score['service_score__avg'],
        'checkin_score': checkin_score['checkin_score__avg'],
        'food_score': food_score['food_score__avg'],
    }
    return Response(review_score)


@api_view(['GET'])
def review_keyword(request, airline_id):
    # file = open('https://j5a203.p.ssafy.io/static/airlines/npl/stopwords.txt', 'r')
    # stopwords = file.read()
    # stopwords = stopwords.split('\n')
    reviews = get_list_or_404(Review, airline=airline_id)

    airline_review = ""
    for review in reviews:
        airline_review += review.content.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
        airline_review += review.title.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

    # # konlpy ver. =============================================================
    # # 말뭉치 (형태소랑 품사 짝)
    # from konlpy.tag import Okt
    # reviews = Okt()
    # morphs = reviews.pos(airline_review)
    
    # noun_adj_list = []
    # for word, tag in morphs:
    #     if (tag in['Noun'] or tag in['Adjective']) and word:
    #         noun_adj_list.append(word)

    # komoran ver. =============================================================
    from PyKomoran import Komoran, DEFAULT_MODEL
    komoran = Komoran(DEFAULT_MODEL['LIGHT'])
    target_tags = ['NNG', 'VA']
    noun_adj_list = komoran.get_morphes_by_tags(airline_review, tag_list=target_tags)

    #빈도수로 정렬하고 단어와 빈도수를 딕셔너리로 전달
    count = Counter(noun_adj_list)
    words = dict(count.most_common())

    # 딕셔너리를 제이슨으로 변환하여 전달
    return HttpResponse(json.dumps(words))
    # return HttpResponse(json.dumps(words), content_type = 'application/json; charset=utf8')

