from django.urls import path, include
from rest_framework import routers

from .views import Buyer_detail, Course_detail

router = routers.DefaultRouter()
router.register(r'Buyer', Buyer_detail)
router.register(r'course', Course_detail)


urlpatterns = [
    path('', include(router.urls)),

]
