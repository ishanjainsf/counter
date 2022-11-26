from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_current_counter, name="currentCounter"),
    path("increment-counter", views.increment_counter, name="incrementCounter")
]