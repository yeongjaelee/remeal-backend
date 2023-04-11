import graphene
from django.core.exceptions import ObjectDoesNotExist
from graphql_jwt.refresh_token.models import RefreshToken
from graphql_jwt.shortcuts import get_token, create_refresh_token

from user.models import User


class GetToken(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()
    email = graphene.String()

    @classmethod
    def mutate(cls, _, __, email):
        try:
            user = User.objects.get(email=email)
            token = get_token(user)
            refresh_token_instance = create_refresh_token(user)
            refresh_token = refresh_token_instance.token
            user.refresh_token = refresh_token
            print(user.refresh_token)
            user.save()
            return GetToken(success=True, token=token, refresh_token=refresh_token, email=email)
        except ObjectDoesNotExist:
            return GetToken(success=False)

