import graphene

import test.schema
import user.schema
import graphql_jwt

class Query(test.schema.Query,
            user.schema.Query):
    pass


class Mutation(test.schema.Mutation,
               user.schema.Mutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)