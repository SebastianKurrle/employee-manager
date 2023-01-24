from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('create/', CompanyView.as_view())
]
