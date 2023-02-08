from django.urls import path, include
from rest_framework import routers

from Learn_IM.Course_app.api.views import Buyer_detail

router = routers.DefaultRouter()
router.register(r'Buyer', Buyer_detail)


urlpatterns = [
    path('', include(router.urls)),

]
