import graphene
from graphene_file_upload.scalars import Upload

from post.models import Post, PostImage


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, title, content):
        print(title)
        print(content)
        post = Post.objects.create(title=title, content=content)
        return CreatePost(success=True)
