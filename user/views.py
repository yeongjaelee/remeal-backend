from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token

from user.models import User


def confirm_email(request):
    try:
        token = request.GET.get('token')
        user_id = request.GET.get('user_id')
        user = User.objects.get(pk=user_id)
        if token == user.token:
            user.token = None
            user.is_active = True
            token = get_token(user)
            refresh_token_instance = create_refresh_token(user)
            refresh_token = refresh_token_instance.token
            user.refresh_token = refresh_token
            user.save()
            print(refresh_token)
            print(token)
            print(user.email)
            return redirect('http://localhost:3000?token={}&refreshToken={}&email={}'.format(token,refresh_token,user.email))
    except ObjectDoesNotExist:
        return redirect('https://www.naver.com/')
