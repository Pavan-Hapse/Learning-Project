from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('Course_app.api.urls')),
    path('middlewareoperations/', 'Course_operation'),

]
