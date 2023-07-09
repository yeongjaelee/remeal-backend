import datetime
import time
import graphene
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
import jwt
from user.models import User

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
        user = User.objects.filter(email=email, is_active=True).first()
        if user:
            pass
        else:
            username, _, _ = email.partition('@')
            user = User.objects.create_user(
                email=email,
                password=None,
                is_active=False,
                username=username
            )
        subject = 'Verify your email'
        token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
                            'user_id': user.id}, 're-meal', algorithm="HS256")
        refresh_token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                                    'user_id': user.id,
                                    'iat': int(time.time())}, 're-meal', algorithm="HS256")
        confirmation_url = f"https://dev.re-meal.com/confirm-email/?token={token}&refresh_token={refresh_token}&user_id={user.id}"
        html_message = render_to_string('../templates/message.html', {'verification_link': confirmation_url,
                                                                      'user_id': user.id,
                                                                      'token': token,
                                                                      'refresh_token': refresh_token})
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



