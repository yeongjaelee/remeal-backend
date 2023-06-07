from django.urls import path

from user import views
from user.views import kakao_view, kakao_info, kakao_info_admin

urlpatterns = [
    path('confirm-email/', views.confirm_email, name='confirm_email'),
    path('kakao/', kakao_view.as_view(), name='kakao_login'),
    path('kakao-info/', kakao_info, name='kakao_info'),
    path('kakao-info-admin/', kakao_info_admin, name='kakao_info_admin')
]
