import graphene
import jwt

from user.models import User


class UserNameUpdate(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        name = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, token, name):
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        user = User.objects.get(pk=user_id)
        user.username = name
        user.save()

        return UserNameUpdate(success=True)