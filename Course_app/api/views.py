from rest_framework import viewsets

from .serializers import BuyerModelSerializer
from .serializers import CourseModelSerializer
from ..models import BuyerModel, CourseModel


class Buyer_detail(viewsets.ModelViewSet):
    serializer_class = BuyerModelSerializer
    queryset = BuyerModel.objects.all()


class Course_detail(viewsets.ModelViewSet):
    serializer_class = CourseModelSerializer
    queryset = CourseModel.objects.all()
