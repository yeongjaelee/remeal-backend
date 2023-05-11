import graphene
import jwt
import time
import datetime

from user.models import User


class CheckToken(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        refresh_token = graphene.String()

    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()
    @classmethod
    def mutate(cls, _, __, token, refresh_token):
        try:
            decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
            refresh_decoded_token = jwt.decode(refresh_token, 're-meal', algorithms="HS256")
            print(refresh_decoded_token['iat'])
            if refresh_decoded_token['iat'] < time.time() - 1296000:
                refresh_token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                                            'user_id': decoded_token['user_id'],
                                            'iat': int(time.time())}, 're-meal', algorithm="HS256")
                user = User.objects.get(pk=decoded_token['user_id'])
                user.refresh_token = refresh_token
                user.save()
                return CheckToken(success=True, refresh_token=refresh_token)
            return CheckToken(success=True)
        except jwt.ExpiredSignatureError as e:
            expired_token = e
            user_id = expired_token['user_id']
            user = User.objects.get(pk=user_id)
            if user.refresh_token == refresh_token:
                token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
                                    'user_id': user.id}, 're-meal', algorithm="HS256")
                return CheckToken(success=True, token=token)
            return CheckToken(success=False)
        else:
            return CheckToken(success=False)
        return CheckToken(success=True)