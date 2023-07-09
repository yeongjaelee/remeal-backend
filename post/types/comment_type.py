import graphene
from graphene_django import DjangoObjectType

from post.models import Comment
from user.models import UserImage
from user.types.UserType import UserType
from user.types.user_image import UserImageType


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

    user_image = graphene.Field(UserImageType)
    @staticmethod
    def resolve_user_image(root, _):
        print(1)
        user_image = UserImage.objects.filter(user=root.user).first()
        print(user_image.image)
        return user_image
