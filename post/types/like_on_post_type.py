from graphene_django import DjangoObjectType

from post.models import LikeOnPost


class LikeOnPostType(DjangoObjectType):
    class Meta:
        model = LikeOnPost
