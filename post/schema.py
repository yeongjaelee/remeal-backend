import graphene

from post.models import Post
from post.mutations.create_post import CreatePost
from post.mutations.upload_image import UploadImage
from post.types.post_type import PostType


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int())
    post_list = graphene.List(PostType, limit=graphene.Int(), tag_name=graphene.String())
    all_post = graphene.Int()
    @staticmethod
    def resolve_post_list(_, __, **kwargs):
        limit = kwargs.get('limit')
        tag_name = kwargs.get('tag_name')
        print(tag_name)
        if tag_name:
            posts = Post.objects.filter(tags__name__icontains=tag_name).order_by('date_created').distinct()[:limit]
            return posts
        else:
            return Post.objects.all().order_by('date_created')[:limit]
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


schema = graphene.Schema(query=Query, mutation=Mutation)
