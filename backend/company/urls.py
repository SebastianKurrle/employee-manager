from django.urls import path
from .views import CompanyView, CompanyDetailView

urlpatterns = [
    path('create/', CompanyView.as_view()),
    path('all/', CompanyView.as_view()),
    path('get/<slug:comp_slug>/', CompanyDetailView.as_view())
]
