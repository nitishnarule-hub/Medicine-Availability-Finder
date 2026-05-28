from django.urls import path
from .views import search_medicine

urlpatterns = [
    path("", search_medicine, name="search"),
]
