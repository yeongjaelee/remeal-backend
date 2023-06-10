import graphene
import jwt
from graphene_file_upload.scalars import Upload

from post.models import Post, PostImage, Tag
from user.models import User


class CreatePost(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        title = graphene.String()
        content = graphene.String()
        images = graphene.List(Upload)
        tags_name = graphene.List(graphene.String)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, info, **kwargs):
        print(1)
        token = kwargs.get('token')
        title = kwargs.get('title')
        content = kwargs.get('content')
        images = kwargs.get('images')
        tags_name = kwargs.get('tags_name')
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user = User.objects.get(pk=decoded_token['user_id'])
        post = Post.objects.create(user=user, title=title, content=content)
        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        if tags_name:
            for tag_name in tags_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tag.posts.add(post)

        return CreatePost(success=True)
