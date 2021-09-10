from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('usermodelview',UserModelViewSet,)
router.register('projectmodelview',ProjectModelViewSet,)
router.register('listsmodelview',ListsModelViewSet,)
router.register('cardsmodelview',CardsModelViewSet,)
urlpatterns= [

    path('user_login/',LoginClass.as_view(),name='user_login'),
    path('',include(router.urls)),

]