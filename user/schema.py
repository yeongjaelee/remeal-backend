import graphene
import jwt

from user.models import User
from user.mutations.check_refresh_token import CheckRefreshToken
from user.mutations.check_token import CheckToken
from user.mutations.check_user import CheckUser
from user.mutations.get_token import GetToken
from user.mutations.profile.delete_user_image import DeleteUserImage
from user.mutations.profile.user_content_mutation import UserContentMutation
from user.mutations.profile.user_image_mutation import UserImageMutation
from user.mutations.profile.user_name_update import UserNameUpdate
from user.types.UserType import UserType


class Query(graphene.ObjectType):
    users = graphene.List(UserType, email_contain=graphene.String())
    user = graphene.Field(UserType, token=graphene.String())

    @staticmethod
    def resolve_user(_, __, token):
        decoded_token = jwt.decode(token, 're-meal', algorithms="HS256")
        user_id = decoded_token['user_id']
        user = User.objects.get(pk=user_id)
        return user
    @staticmethod
    def resolve_users(_, info, email_contain):
        user = info.context.user
        print(user.id)
        return User.objects.filter(email__icontains=email_contain)

class Mutation(graphene.ObjectType):
    check_user = CheckUser.Field()
    get_token = GetToken.Field()
    check_refresh_token = CheckRefreshToken.Field()
    check_token = CheckToken.Field()
    user_content_mutation = UserContentMutation.Field()
    user_image_mutation = UserImageMutation.Field()
    delete_user_image = DeleteUserImage.Field()
    user_name_update = UserNameUpdate.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)
