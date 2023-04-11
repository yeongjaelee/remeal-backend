from graphene import relay
from graphene_django import DjangoObjectType

from user.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


