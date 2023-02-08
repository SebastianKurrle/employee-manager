from django.urls import path
from .views import CompanyView, CompanyDetailView

urlpatterns = [
    path('company/create/', CompanyView.as_view()),
    path('company/all/', CompanyView.as_view()),
    path('company/get/<slug:comp_slug>/', CompanyDetailView.as_view()),
    path('company/<int:id>/', CompanyDetailView.as_view())
]
