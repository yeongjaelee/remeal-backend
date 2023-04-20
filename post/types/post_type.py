import graphene
from graphene_django import DjangoObjectType

from post.models import Post
from post.types.post_image_type import PostImageType


class PostType(DjangoObjectType):
    class Meta:
        model = Post

    first_post_image = graphene.Field(PostImageType)

    @staticmethod
    def resolve_first_post_image(root, _):
        first_post_image = root.images.all().order_by('id').first()
        return first_post_image