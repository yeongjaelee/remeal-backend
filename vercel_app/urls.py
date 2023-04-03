"""vercel_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import ConfirmEmailView
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from user.models import user

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include('user.urls')),
    # path('signup/', signup, name='signup'),
]
