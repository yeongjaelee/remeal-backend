import graphene
from graphene_django import DjangoObjectType

from post.models import Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag