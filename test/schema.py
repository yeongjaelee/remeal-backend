import graphene

from test.mutations.test_mutation import TestMutation
from test.types.post_type import PostType


class Query(graphene.ObjectType):
    test_query = graphene.Field(PostType)


class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
