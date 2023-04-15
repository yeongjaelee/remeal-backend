import graphene

from post.mutations.create_post import CreatePost
from post.mutations.upload_image import UploadImage


class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    upload_image = UploadImage.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
