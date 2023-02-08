from django.contrib import admin
from .models import BuyerModel, CourseModel

# Register your models here.

admin.site.register(CourseModel)
admin.site.register(BuyerModel)