import graphene
from django.core.mail import EmailMessage

class TestMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, email):
        print('email is')
        print(email)
        email = EmailMessage('test email title', 'test email content', to=[email])
        email.send()
        return TestMutation(success=True)

