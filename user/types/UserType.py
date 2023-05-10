import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from user.models import User
from user.types.UserContentType import UserContentType


class UserType(DjangoObjectType):
    class Meta:
        model = User

    user_content = graphene.Field(UserContentType)

    @staticmethod
    def resolve_user_content(root, _):
        print(root.contents.all().first())
        return root.contents.all().first()


