import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from user.models import User
from user.types.UserContentType import UserContentType
from user.types.user_image import UserImageType


class UserType(DjangoObjectType):
    class Meta:
        model = User

    user_content = graphene.Field(UserContentType)
    user_image = graphene.Field(UserImageType)
    @staticmethod
    def resolve_user_content(root, _):
        return root.contents.all().first()

    @staticmethod
    def resolve_user_image(root, _):
        return root.image.all().first()

