from graphene_django import DjangoObjectType

from post.models import Comment


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
