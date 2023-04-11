import os

import graphene
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from graphql_jwt.decorators import login_required
from graphql_jwt.refresh_token.shortcuts import create_refresh_token

from user.methods.message import message
from user.models import User
from graphql_jwt.shortcuts import get_token


class CheckUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()
    email = graphene.String()
    message = graphene.String()
    @classmethod
    def mutate(cls, _, __, email):
        print(email)
        print('hello')
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                token = get_token(user)
                refresh_token_instance = create_refresh_token(user)
                refresh_token = refresh_token_instance.token
                user.refresh_token = refresh_token
                print(user.refresh_token)
                user.save()
                return CheckUser(success=True, token=token, refresh_token=refresh_token, email=email, message="로그인완료")
            else:
                return CheckUser(success=False)
        except ObjectDoesNotExist:
            subject = 'Verify your email'
            user = User.objects.create_user(
                email=email,
                password=None,
                is_active=False
            )
            verification_token = user.generate_verification_token()
            user.token = verification_token
            user.save()
            confirmation_url = f"http://127.0.0.1:8000/confirm-email/?token={verification_token}&user_id={user.id}"
            html_message = render_to_string('../templates/message.html', {'verification_link': confirmation_url,
                                                                          'user_id': user.id,
                                                                          'verification_token': verification_token})
            # Send the email
            send_mail(
                subject,
                "hello",
                'yeongjae.blocket@example.com',  # replace with your email address
                [email],
                fail_silently=False,
                html_message=html_message
            )
            print(11)
            return CheckUser(success=False, token=None)

