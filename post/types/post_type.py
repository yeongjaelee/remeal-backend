import graphene
from graphene_django import DjangoObjectType

from post.models import Post
from post.types.post_image_type import PostImageType
from post.types.tag_type import TagType


class PostType(DjangoObjectType):
    class Meta:
        model = Post

    first_post_image = graphene.Field(PostImageType)
    all_number = graphene.Int()
    date_created_year = graphene.String()
    date_created_month = graphene.String()
    date_created_day = graphene.String()
    tags_on_post = graphene.List(TagType)

    @staticmethod
    def resolve_tags_on_post(root, _):
        return root.tags.all()
    @staticmethod
    def resolve_first_post_image(root, _):
        first_post_image = root.images.all().order_by('id').first()
        return first_post_image

    @staticmethod
    def resolve_all_number(root, _):
        return Post.objects.count()

    @staticmethod
    def resolve_date_created_year(root, _):
        return root.date_created.year
    @staticmethod
    def resolve_date_created_month(root, _):
        if root.date_created.month < 10:
            number_with_zeros = '{:02d}'.format(root.date_created.month)
        else:
            number_with_zeros = root.date_created.month
        return number_with_zeros
    @staticmethod
    def resolve_date_created_day(root, _):
        if root.date_created.month < 10:
            number_with_zeros = '{:02d}'.format(root.date_created.day)
        else:
            number_with_zeros = root.date_created.day
        return number_with_zeros

