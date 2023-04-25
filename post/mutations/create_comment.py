import graphene
import jwt

from post.models import Post, Comment
from post.types.comment_type import CommentType


class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int()
        token = graphene.String()
        comment = graphene.String()

    success = graphene.Boolean()
    is_writer = graphene.Boolean()
    comments = graphene.List(CommentType)
    @classmethod
    def mutate(cls, _, __, post_id, token, comment):
        post = Post.objects.get(pk=post_id)
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        if user_id == post.user.id:
            is_writer = True
            print(1)
            print(user_id)
        else:
            is_writer = False
            print(2)
            print(user_id)
        comment = Comment.objects.create(post=post, user_id=user_id, comment=comment)
        comments = comment.post.comments.all().order_by('-date_created')
        return CreateComment(success=True, is_writer=is_writer, comments=comments)