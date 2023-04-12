import graphene

from test.types.post_type import PostType
from user.models import User
from user.mutations.check_refresh_token import CheckRefreshToken
from user.mutations.check_token import CheckToken
from user.mutations.check_user import CheckUser
from user.mutations.get_token import GetToken
from user.types.UserType import UserType


class Query(graphene.ObjectType):
    test_query = graphene.Field(PostType)
    users = graphene.List(UserType, email_contain = graphene.String() )
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


schema = graphene.Schema(query=Query, mutation=Mutation)
