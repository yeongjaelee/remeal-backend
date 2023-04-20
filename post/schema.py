import graphene

from post.models import Post
from post.mutations.create_post import CreatePost
from post.mutations.upload_image import UploadImage
from post.types.post_type import PostType


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int())
    post_list = graphene.List(PostType, limit=graphene.Int())

    @staticmethod
    def resolve_post_list(_, __, limit):
        return Post.objects.all()[:limit]
    @staticmethod
    def resolve_post(_, info, id):
        post = Post.objects.get(pk=id)
        print(post.title)
        return post

class Mutation(graphene.ObjectType):
    upload_image = UploadImage.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
