from django.urls import path, include
from . import views
#from .views import Another
from rest_framework import routers
from .views import PaperViewSet, PptViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('papers', PaperViewSet) #REST ali path deer haragdah route-iig zaaj ugnus
router.register('ppts', PptViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('another', Another.as_view())
]
