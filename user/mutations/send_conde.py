import graphene

class SendConde(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, number):
        print(number)
        return SendConde(success=True)