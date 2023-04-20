import graphene
from graphene_file_upload.scalars import Upload

from post.models import Post, PostImage


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()
        images = graphene.List(Upload)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, title, content, images):
        print(title)
        print(content)
        post = Post.objects.create(title=title, content=content)
        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        return CreatePost(success=True)
