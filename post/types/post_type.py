import graphene
import jwt
from graphene_django import DjangoObjectType

from post.models import Post, LikeOnPost
from post.types.comment_type import CommentType
from post.types.like_on_post_type import LikeOnPostType
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
    date_created_hour = graphene.String()
    date_created_minute = graphene.String()
    tags_on_post = graphene.List(TagType)
    comments = graphene.List(CommentType)
    like_number = graphene.Int()
    is_like_user = graphene.Field(LikeOnPostType, token=graphene.String())
    is_mine = graphene.Boolean(token=graphene.String())

    @staticmethod
    def resolve_is_mine(root, __, token):
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        if root.user.id == user_id:
            return True
        else:
            return False
    @staticmethod
    def resolve_is_like_user(root, info,token):
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        like_on_post = LikeOnPost.objects.filter(user_id=user_id, post_id=root.id).first()

        return like_on_post
    @staticmethod
    def resolve_like_number(root, _):
        return root.likes.filter(is_like=True).count()
    @staticmethod
    def resolve_comments(root,_):
        return root.comments.all()
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
        if root.date_created.day < 10:
            number_with_zeros = '{:02d}'.format(root.date_created.day)
        else:
            number_with_zeros = root.date_created.day
        return number_with_zeros

    @staticmethod
    def resolve_date_created_hour(root, _):
        if root.date_created.hour < 10:
            number_with_zeros = '{:02d}'.format(root.date_created.hour)
        else:
            number_with_zeros = root.date_created.hour
        return number_with_zeros

    @staticmethod
    def resolve_date_created_minute(root, _):
        if root.date_created.minute < 10:
            number_with_zeros = '{:02d}'.format(root.date_created.minute)
        else:
            number_with_zeros = root.date_created.minute
        return number_with_zeros
