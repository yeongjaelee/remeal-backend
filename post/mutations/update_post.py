import graphene
from graphene_file_upload.scalars import Upload

from post.models import Post, Tag, PostImage


class UpdatePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int()
        title = graphene.String()
        content = graphene.String()
        images = graphene.List(Upload)
        tags_name = graphene.List(graphene.String)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, info, **kwargs):
        post_id = kwargs.get('post_id')
        title = kwargs.get('title')
        content = kwargs.get('content')
        images = kwargs.get('images')
        tags_name = kwargs.get('tags_name')
        post = Post.objects.get(pk=post_id)
        post.title = title
        post.content = content
        post.save()
        post.images.exclude(image__in=images).delete()
        old_post_images = post.images.filter(image__in=images)
        for old_post_image in old_post_images:
            if old_post_image.image in images:
                images.remove(old_post_image.image)
        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        post.tags.clear()
        if tags_name:
            for tag_name in tags_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tag.posts.add(post)
        return UpdatePost(success=True)