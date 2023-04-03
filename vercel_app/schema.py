import graphene

import test.schema
import user.schema


class Query(test.schema.Query,
            user.schema.Query):
    pass


class Mutation(test.schema.Mutation,
               user.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)