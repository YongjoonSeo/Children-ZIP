from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')), # rest_auth url 등록
    path('rest-auth/registration/', include('rest_auth.registration.urls')), # 회원가입
    path('community/', include('community.urls')),
]
