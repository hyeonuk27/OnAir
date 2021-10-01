from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .utils import check_login

from decouple import config
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import string
import random
import requests
import jwt

JWT_SECRET_KEY = config('JWT_SECRET_KEY')

User = get_user_model()

def make_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(13))


@api_view(['GET'])
def login(request):
    token = request.headers["Authorization"]
    url = 'https://oauth2.googleapis.com/tokeninfo?id_token='
    response = requests.get(url+token)
    user = response.json()

    # 로그인
    if User.objects.filter(google_id = user['sub']).exists():
        user_info = User.objects.get(google_id=user['sub'])
        encoded_jwt = jwt.encode({'id': user["sub"]}, JWT_SECRET_KEY, algorithm='HS256')
        serializer = UserSerializer(user_info)
    # 회원가입
    else:
        while True:
            user_id = make_random_id()
            if(User.objects.filter(id=id).exists()):
                continue
            else:
                break
        new_user = User(
            id = user_id,
            name = user.get('name'),
            username = user.get('name'),
            email = user.get('email'),
            google_id = user.get('sub'),
            profile_url = user.get('picture')
        )
        new_user.save()
        serializer = UserSerializer(new_user)
        encoded_jwt = jwt.encode({'id': new_user.id}, JWT_SECRET_KEY, algorithm='HS256')
    data = {
        'info': serializer.data,
        'access_token': encoded_jwt,
    }
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@check_login
def update(request):
    serializer = UserSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)