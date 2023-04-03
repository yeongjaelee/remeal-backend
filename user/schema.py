import graphene

from test.types.post_type import PostType
from user.mutations.check_user import CheckUser


class Query(graphene.ObjectType):
    test_query = graphene.Field(PostType)


class Mutation(graphene.ObjectType):
    check_user = CheckUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
