from django.contrib import admin
from .models import BuyerModel, CourseModel, InstituteModel, CountryModel, StateModel, AddressModel

# Register your models here.

admin.site.register(CourseModel)
admin.site.register(BuyerModel)
admin.site.register(InstituteModel)
admin.site.register(CountryModel)
admin.site.register(StateModel)
admin.site.register(AddressModel)
