import graphene
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token

from user.models import User


class CheckRefreshToken(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        refresh_token = graphene.String()

    success = graphene.Boolean()
    refresh_token = graphene.String()
    token = graphene.String()

    @classmethod
    def mutate(cls, _, __, email, refresh_token):
        try:
            user = User.objects.get(email=email)
            if user.refresh_token == refresh_token:
                new_token = get_token(user)
                new_refresh_token_instance = create_refresh_token(user)
                new_refresh_token = new_refresh_token_instance.token
                user.refresh_token = new_refresh_token
                user.save()
                return CheckRefreshToken(success=True, token=new_token, refresh_token=new_refresh_token)
        except User.DoesNotExist:
            return CheckRefreshToken(success=False)