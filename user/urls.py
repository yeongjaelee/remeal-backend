from django.urls import path

from user import views

urlpatterns = [
    path('confirm-email/', views.confirm_email, name='confirm_email'),
    path('kakao/', views.kakao_login, name='kakao_login')
]
