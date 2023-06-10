import graphene
from graphene_django import DjangoObjectType

from user.models import UserContent


class UserContentType(DjangoObjectType):
    class Meta:
        model = UserContent
