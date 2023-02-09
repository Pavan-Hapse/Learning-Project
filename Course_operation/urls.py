from django.urls import path, include
from .views import User, dummy

urlpatterns = [
    path('list/', User),
    path('dummy/', dummy),

]