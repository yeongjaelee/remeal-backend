import graphene

from post.models import Post
from post.mutations.create_comment import CreateComment
from post.mutations.create_post import CreatePost
from post.mutations.like_on_post_mutation import LikeOnPostMutation
from post.mutations.upload_image import UploadImage
from post.types.comment_type import CommentType
from post.types.post_type import PostType


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int(), token=graphene.String())
    post_list = graphene.List(PostType, limit=graphene.Int(), offset=graphene.Int(), tag_name=graphene.String())
    all_post = graphene.Int()
    comments = graphene.List(CommentType, post_id=graphene.Int())

    @staticmethod
    def resolve_comments(_, __, post_id):
        post = Post.objects.get(pk=post_id)
        comments = post.comments.all().order_by('-date_created')
        return comments

    @staticmethod
    def resolve_post_list(_, __, **kwargs):
        limit = kwargs.get('limit')
        offset = kwargs.get('offset')
        tag_name = kwargs.get('tag_name')
        if tag_name:
            posts = Post.objects.filter(tags__name__exact=tag_name).distinct().order_by('id')[offset:limit]
            return posts
        else:
            return Post.objects.all().order_by('id')[offset:limit]

    @staticmethod
    def resolve_post(_, info, id):
        post = Post.objects.get(pk=id)
        return post

    @staticmethod
    def resolve_all_post(_, info):
        return Post.objects.count()


class Mutation(graphene.ObjectType):
    upload_image = UploadImage.Field()
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
    like_on_post_mutation = LikeOnPostMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
