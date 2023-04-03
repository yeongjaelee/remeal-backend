from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from user.models import User


def confirm_email(request):
    try:
        token = request.GET.get('token')
        user_id = request.GET.get('user_id')
        user = User.objects.get(pk=user_id)
        user.token = token
        return redirect('http://localhost:3000')
    except ObjectDoesNotExist:
        return redirect('https://www.naver.com/')
