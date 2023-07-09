import graphene
from django.shortcuts import redirect


class KakaoLogin(graphene.Mutation):
    success = graphene.Boolean()
    url = graphene.String()


    @classmethod
    def mutate(cls, _, __):
        client_id = 'f6b986215c4dc13b37c8ca0e4e57ad26'
        kakao_auth_id = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = "https://dev.re-meal.com/kakao-info"

        return KakaoLogin(success=True,
                          url=f"{kakao_auth_id}&client_id={client_id}&redirect_uri={redirect_uri}"
                         )

