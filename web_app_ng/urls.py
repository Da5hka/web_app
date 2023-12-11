from django.urls import path, include
from . import views
from .views import Another
from rest_framework import routers
from .views import NgViewSet

router = routers.DefaultRouter()
router.register('informations', NgViewSet) #REST ali path deer haragdah route-iig zaaj ugnus


urlpatterns = [
    path('', include(router.urls)),
    path('another', Another.as_view())
]
