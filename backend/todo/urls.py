from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import TodoViewsets

router = DefaultRouter()
router.register(r'', TodoViewsets)

urlpatterns = [
    path('', include(router.urls)),
]