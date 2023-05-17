from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token

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


def kakao_login(request):
    print(1111)
    client_id = 'f6b986215c4dc13b37c8ca0e4e57ad26'
    kakao_auth_id = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    redirect_uri = "http://localhost:3000/kakao"

    return redirect(f'{kakao_auth_id}&client_id={client_id}&redirect_uri={redirect_uri}')

