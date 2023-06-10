import graphene
from graphene_django import DjangoObjectType

from post.models import PostImage


class PostImageType(DjangoObjectType):
    class Meta:
        model = PostImage