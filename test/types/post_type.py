import graphene
from graphene_django import DjangoObjectType

from test.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post


