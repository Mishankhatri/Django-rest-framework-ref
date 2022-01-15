"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path 
from django.urls.conf import include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as tokenview
from api.customauthtoken import CustomAuthToken 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = DefaultRouter()
# router.register('studentapi',views.StudentViewSet,basename='student')
# router.register('modelviewsetApi',views.StudentModelViewSet,basename='studentmodelviewset')
# router.register('readonlyviewsetApi',views.StudentReadOnlyModelViewSet,basename='studentreadonlymodelviewset')
router.register('songs',views.SongModelViewSet,basename='song')
router.register('singers',views.SingerModelViewSet,basename='singer')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    # path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    # path('api/gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    # path("gettoken/", tokenview.obtain_auth_token, name="gettoken"),
    # path("gettoken/", CustomAuthToken.as_view(), name="gettoken"),
    # basic jsonresponse api
    # path('stuinfo/<int:pk>',views.student_detail),
    # path('stuinfo/',views.studentAll),
    # path('stucreate/',views.student_create),
    # path('studentapi/',views.student_api),
    # path('api/',views.StudentApi.as_view(),name='api'),
    
    # # DRF apiview decorators and APIView class
    # path("hello/", views.hello_world, name="helloworld"),
    # path("fxnapi/", views.fxnapi, name="fxnapi_withapiview"),
    # path("fxnapi/<int:pk>", views.fxnapi, name="fxnapi_withapiview"),
    # path("classapi/", views.ClassApi.as_view(), name="classapi_withapiview"),
    # path("classapi/<int:pk>", views.ClassApi.as_view(), name="classapi_withapiview"),
    
    # #DRF GenereicAPIView and mixins
    # path("mixins/", views.LCmixins.as_view(), name="lcmixins"),
    # path("mixins/<int:pk>", views.RUDmixins.as_view(), name="rudmixins"),
    
    # #DRF ConcreteViews
    # path("apiviews/", views.StudentListCreateAPIView.as_view(), name="listcreateview"),
    # path("apiviews/<int:pk>", views.StudentRetrieveUpdateDestroyAPIView.as_view(), name="rudview")
]
