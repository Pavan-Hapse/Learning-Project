from django.db import models


# Create your models here.

class BuyerModel(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    mobile_number = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class CourseModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.BooleanField(null=False, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
