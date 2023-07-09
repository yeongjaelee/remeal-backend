import graphene
import jwt
from graphene_file_upload.scalars import Upload

from user.models import User, UserImage


class UserImageMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        image = Upload()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __ , **kwargs):
        token = kwargs.get('token')
        image = kwargs.get('image')
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        user = User.objects.get(pk=user_id)
        user_image = UserImage.objects.filter(user=user).first()
        if user_image:
            user_image.image = image
            user_image.is_deleted = False
            user_image.save()
        else:
            UserImage.objects.create(user=user, image=image)
        print('upload image')
        return UserImageMutation(success=True)