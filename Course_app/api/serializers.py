from rest_framework import serializers
from .model import BuyerModel, CourseModel


class BuyerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerModel
        fields = "__all__"


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"