import graphene
from graphene_django import DjangoObjectType

from user.models import UserImage


class UserImageType(DjangoObjectType):
    class Meta:
        model = UserImage

