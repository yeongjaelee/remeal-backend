import graphene

from post.models import Post
from post.mutations.create_comment import CreateComment
from post.mutations.create_post import CreatePost
from post.mutations.like_on_post_mutation import LikeOnPostMutation
from post.mutations.update_post import UpdatePost
from post.mutations.upload_image import UploadImage
from post.types.comment_type import CommentType
from post.types.post_type import PostType
from user.models import User


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int(), token=graphene.String())
    post_list = graphene.List(PostType, limit=graphene.Int(), offset=graphene.Int(), tag_name=graphene.String(), email=graphene.String())
    all_post = graphene.Int()
    comments = graphene.List(CommentType, post_id=graphene.Int())
    my_posts = graphene.List(PostType, email=graphene.String())

    # @staticmethod
    # def resolve_my_posts(_, __, ):
    #     user = User.objects.get(email=email)
    #     posts = Post.objects.filter(user=user)
    #     return posts
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
        email = kwargs.get('email')

        if tag_name:
            if email:
                posts = Post.objects.filter(tags__name__exact=tag_name, user__email=email).distinct().order_by('id')[offset:limit]
                return posts
            else:
                posts = Post.objects.filter(tags__name__exact=tag_name).distinct().order_by('id')[offset:limit]
                return posts
        else:
            if email:
                return Post.objects.filter(user__email=email).order_by('id')[offset:limit]
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
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    like_on_post_mutation = LikeOnPostMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
