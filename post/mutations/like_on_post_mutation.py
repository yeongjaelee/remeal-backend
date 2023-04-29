import graphene
import jwt
from post.models import LikeOnPost, Post


class LikeOnPostMutation(graphene.Mutation):
    print(111111)
    class Arguments:
        token = graphene.String()
        post_id = graphene.Int()
        is_like = graphene.Boolean()
    print(111)
    success = graphene.Boolean()
    like_number = graphene.Int()
    is_like_result = graphene.Boolean()
    @classmethod
    def mutate(cls, _, __, token, post_id, is_like):
        print(11)
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        like_on_post, created = LikeOnPost.objects.get_or_create(user_id=user_id,
                                                                 post_id=post_id)
        like_on_post.is_like = is_like
        like_on_post.save()
        post = Post.objects.get(pk=post_id)
        like_number = post.likes.filter(is_like=True).count()
        is_like_result = like_on_post.is_like
        return LikeOnPostMutation(success=True, like_number=like_number, is_like_result=is_like_result)