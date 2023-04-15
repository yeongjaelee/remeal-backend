import graphene

import post.schema
import user.schema
import graphql_jwt


class Query(post.schema.Query,
            user.schema.Query):
    pass


class Mutation(post.schema.Mutation,
               user.schema.Mutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)