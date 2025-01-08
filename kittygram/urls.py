from rest_framework.routers import SimpleRouter
from django.urls import path, include

from cats.views import CatViewSet


router = SimpleRouter()

router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
