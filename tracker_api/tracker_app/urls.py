from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

app_name="tracker_app"

router=DefaultRouter()
router.register(r'user',UserModelViewSet,)
router.register(r'project',ProjectModelViewSet,)
# router.register('lists',ListsModelViewSet,)
router.register(r'cards',CardsModelViewSet,)
urlpatterns= [

    path('',include(router.urls)),
    path(r'login/', oauth_redirect, name='oauth_redirect'),
    path(r'login1/', login1, name='login1'),

]