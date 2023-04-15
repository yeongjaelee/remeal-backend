import graphene
from graphene_django import DjangoObjectType

from post.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post