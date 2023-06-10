import jwt
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import View
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token
import datetime, time
from user.models import User


def confirm_email(request):
    try:
        token = request.GET.get('token')
        user_id = request.GET.get('user_id')
        refresh_token = request.GET.get('refresh_token')
        user = User.objects.get(pk=user_id)
        user_email_first = user.email[0]
        user.is_active = True
        user.refresh_token = refresh_token
        user.save()
        return redirect('http://localhost:3000?token={}&refreshToken={}&userEmailFirst={}'.format(token, refresh_token,user_email_first))
    except ObjectDoesNotExist:
        return redirect('http://localhost:3000')


class kakao_view(View):
    def get(self, request):
        print(1111)
        client_id = 'f6b986215c4dc13b37c8ca0e4e57ad26'
        kakao_auth_id = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = "http://127.0.0.1:8000/kakao-info"
        print(request)
        print(22222)
        return redirect(f'{kakao_auth_id}&client_id={client_id}&redirect_uri={redirect_uri}')

def kakao_info(request):
    code = request.GET.get('code')
    is_user = request.GET.get('is_user')
    print('--is_user--')
    print(is_user)
    print('--is_user--')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token',
    data = {
        'grant_type': 'authorization_code',
        'client_id': 'f6b986215c4dc13b37c8ca0e4e57ad26',
        'redirection_uri': "http://127.0.0.1:8000/kakao-info",
        'code': code
    }
    token_response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
    access_token = token_response.json().get('access_token')
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f'Bearer ${access_token}'}).json()
    email = user_info['kakao_account']['email']
    user = User.objects.filter(email=email).first()
    token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
                        'user_id': user.id}, 're-meal', algorithm="HS256")
    refresh_token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                                'user_id': user.id,
                                'iat': int(time.time())}, 're-meal', algorithm="HS256")
    if user:
        user.is_active = True
        user.refresh_token = refresh_token
    else:
        username, _, _ = email.partition('@')
        user = User.objects.create_user(
            email=email,
            password=None,
            is_active=True,
            username=username
        )
        user.refresh_token = refresh_token
    user_email_first = user.email[0]
    user.save()

    return redirect('http://localhost:3000?token={}&refreshToken={}&userEmailFirst={}'.format(token, refresh_token,user_email_first))

def kakao_info_admin(request):
    print('admin 페이지입니다')
    code = request.GET.get('code')
    is_user = request.GET.get('is_user')
    print('--is_user--')
    print(is_user)
    print('--is_user--')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token',
    data = {
        'grant_type': 'authorization_code',
        'client_id': 'f6b986215c4dc13b37c8ca0e4e57ad26',
        'redirection_uri': "http://127.0.0.1:8000/kakao-info",
        'code': code
    }
    token_response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
    access_token = token_response.json().get('access_token')
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f'Bearer ${access_token}'}).json()
    email = user_info['kakao_account']['email']
    user = User.objects.filter(email=email).first()
    token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
                        'user_id': user.id}, 're-meal', algorithm="HS256")
    refresh_token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                                'user_id': user.id,
                                'iat': int(time.time())}, 're-meal', algorithm="HS256")
    if user:
        user.is_active = True
        user.refresh_token = refresh_token
    else:
        username, _, _ = email.partition('@')
        user = User.objects.create_user(
            email=email,
            password=None,
            is_active=True,
            username=username
        )
        user.refresh_token = refresh_token
    user_email_first = user.email[0]
    user.save()

    return redirect('http://localhost:3000?token={}&refreshToken={}&userEmailFirst={}'.format(token, refresh_token,user_email_first))


