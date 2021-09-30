from decouple import config
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

import jwt

JWT_SECRET_KEY = config('JWT_SECRET_KEY')
User = get_user_model()

def check_login(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers["Authorization"]
            user_id = jwt.decode(access_token, JWT_SECRET_KEY, algorithm='HS256')
            user = User.objects.get(id=user_id)
            request.user = user
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN' }, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)
        
        return func(self, request, *args, **kwargs)
    return wrapper 