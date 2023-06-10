import graphene
import jwt

from user.models import User


class DeleteUserImage(graphene.Mutation):
    class Arguments:
        token = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, token):
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        user = User.objects.get(pk=user_id)
        user_image = user.image.all().first()
        if user_image:
            user_image.is_deleted = True
            user_image.save()
        return DeleteUserImage(success=True)
