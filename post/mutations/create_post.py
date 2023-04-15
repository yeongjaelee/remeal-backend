import graphene
from graphene_file_upload.scalars import Upload

from post.models import Post, PostImage


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()
        main_image = Upload
        images = [Upload]

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, **kwargs):
        title = kwargs.get('title')
        content = kwargs.get('content')
        main_image = kwargs.get('main_image')
        images = kwargs.get('images')

        post = Post.objects.create(title=title, content=content, main_image=main_image)
        for image in images:
            PostImage.objects.create(post=post, image=image)

        return CreatePost(success=True)
