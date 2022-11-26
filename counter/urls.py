from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('count/', include('count.urls')),
    path('admin/', admin.site.urls)
]
