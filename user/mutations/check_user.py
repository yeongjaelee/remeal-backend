import os

import graphene
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

from user.methods.message import message
from user.models import User


class CheckUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    success = graphene.Boolean()
    token = graphene.String()

    @classmethod
    def mutate(cls, _, __, email):
        try:
            user = User.objects.get(email=email)
            token = user.token
            user.token = None
            user.save()
            return CheckUser(success=True, token=token)
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
            return CheckUser(success=True)

