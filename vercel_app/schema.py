import graphene

import test.schema


class Query(test.schema.Query):
    pass


class Mutation(test.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)