from rest_framework import serializers

from ..models import BuyerModel, CourseModel, InstituteModel, StateModel, AddressModel,  CountryModel


class BuyerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerModel
        fields = "__all__"


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"


class InstituteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteModel
        fields = "__all__"


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = "__all__"


class StateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        fields = "__all__"


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = "__all__"
