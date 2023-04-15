import graphene

from post.mutations.upload_image import UploadImage


class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    upload_image = UploadImage.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
