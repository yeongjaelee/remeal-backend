import graphene
import jwt
from post.models import LikeOnPost


class LikeOnPostMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        post_id = graphene.Int()
        is_like = graphene.Boolean()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, token, post_id, is_like):
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        like_on_post, created = LikeOnPost.objects.get_or_create(user_id=user_id,
                                                                 post_id=post_id)
        like_on_post.is_like = is_like
        like_on_post.save()

        return LikeOnPostMutation(success=True)