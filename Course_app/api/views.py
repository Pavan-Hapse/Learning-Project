from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters


from .serializers import (CourseModelSerializer, StateModelSerializer, InstituteModelSerializer,
                          CountryModelSerializer, BuyerModelSerializer, AddressModelSerializer)
from ..models import BuyerModel, CourseModel, InstituteModel, AddressModel, StateModel, CountryModel


class Buyer_detail(viewsets.ModelViewSet):
    serializer_class = BuyerModelSerializer
    queryset = BuyerModel.objects.all()
    filter_backends = [ filters.SearchFilter ]
    search_fields = [ 'first_name' ]


class Course_detail(viewsets.ModelViewSet):
    serializer_class = CourseModelSerializer
    queryset = CourseModel.objects.all()
    filter_backends = [ filters.SearchFilter ]
    search_fields = [ 'title']


class InstituteModel_detail(viewsets.ModelViewSet):
    serializer_class = InstituteModelSerializer
    queryset = InstituteModel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'courses__title']             #This field return the particular field data of other table


class AddressModel_detail(viewsets.ModelViewSet):
    serializer_class = AddressModelSerializer
    queryset = AddressModel.objects.all()
    filter_backends = [ filters.SearchFilter ]
    search_fields = [ 'country' ]


class StateModel_detail(viewsets.ModelViewSet):
    serializer_class = StateModelSerializer
    queryset = StateModel.objects.all()
    filter_backends = [ filters.SearchFilter ]
    search_fields = [ 'name']


class CountryModel_detail(viewsets.ModelViewSet):
    serializer_class = CountryModelSerializer
    queryset = CountryModel.objects.all()
    filter_backends = [ filters.SearchFilter ]
    search_fields = [ 'name']

