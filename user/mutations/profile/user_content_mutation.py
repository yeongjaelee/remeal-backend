import graphene
import jwt
from graphene_file_upload.scalars import Upload

from user.models import User, UserContent


class UserContentMutation(graphene.Mutation):
    print(1111)
    class Arguments:
        token = graphene.String()
        content = graphene.String()
        image = Upload()
        is_image_src = graphene.Boolean()
    print(2222)
    success = graphene.Boolean()
    print(3333)
    @classmethod
    def mutate(cls, _, __, **kwargs):
        token = kwargs.get('token')
        content = kwargs.get('content')
        image = kwargs.get('image')
        is_image_src = kwargs.get('is_image_src')
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        user = User.objects.get(pk=user_id)
        user_content = UserContent.objects.filter(user=user).first()
        print(is_image_src)
        print(image)
        if user_content:
            user_content.content = content
            if is_image_src:
                if image:
                    user_content.image = image
            else:
                print(2)
                user_content.image = None
            user_content.save()
        else:
            UserContent.objects.create(user=user, content=content, image=image)
        return UserContentMutation(success=True)

