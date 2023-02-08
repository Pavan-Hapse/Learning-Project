from django.urls import path, include
from rest_framework import routers

from .views import (Buyer_detail, Course_detail, InstituteModel_detail,
                    AddressModel_detail, StateModel_detail, CountryModel_detail)

router = routers.DefaultRouter()
router.register(r'Buyer', Buyer_detail)
router.register(r'courses', Course_detail)
router.register(r'institutes', InstituteModel_detail)
router.register(r'address', AddressModel_detail)
router.register(r'state', StateModel_detail)
router.register(r'country', CountryModel_detail)


urlpatterns = [
    path('', include(router.urls)),

]
