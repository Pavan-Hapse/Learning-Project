from rest_framework import viewsets

from .serializers import (CourseModelSerializer, StateModelSerializer, InstituteModelSerializer,
                          CountryModelSerializer, BuyerModelSerializer, AddressModelSerializer)
from ..models import BuyerModel, CourseModel, InstituteModel, AddressModel, StateModel, CountryModel


class Buyer_detail(viewsets.ModelViewSet):
    serializer_class = BuyerModelSerializer
    queryset = BuyerModel.objects.all()


class Course_detail(viewsets.ModelViewSet):
    serializer_class = CourseModelSerializer
    queryset = CourseModel.objects.all()


class InstituteModel_detail(viewsets.ModelViewSet):
    serializer_class = InstituteModelSerializer
    queryset = InstituteModel.objects.all()


class AddressModel_detail(viewsets.ModelViewSet):
    serializer_class = AddressModelSerializer
    queryset = AddressModel.objects.all()


class StateModel_detail(viewsets.ModelViewSet):
    serializer_class = StateModelSerializer
    queryset = StateModel.objects.all()


class CountryModel_detail(viewsets.ModelViewSet):
    serializer_class = CountryModelSerializer
    queryset = CountryModel.objects.all()
