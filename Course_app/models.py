import uuid

from django.db import models


# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    owner = models.UUIDField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CountryModel(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)


class StateModel(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    county = models.ForeignKey(CountryModel, on_delete=models.PROTECT, null=True, blank=True)


class BuyerModel(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class CourseModel(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    maximum_bookings = models.IntegerField(null=True, blank=True, default=0)
    terms_and_conditions = models.TextField(max_length=1024, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AddressModel(BaseModel):
    country = models.ForeignKey(CountryModel, null=True, blank=True, on_delete=models.PROTECT)
    state = models.ForeignKey(StateModel, on_delete=models.PROTECT)
    city = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=6)
    landmark = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=True)


class InstituteModel(BaseModel):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(CourseModel, blank=True, related_name='course_institutes')
    description = models.CharField(max_length=1024, null=True, blank=True)
    terms_and_conditions = models.TextField(max_length=1024)

    def __str__(self):
        return self.name
