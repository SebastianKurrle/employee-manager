from django.urls import path
from . import views

urlpatterns = [
    path('company/create/', views.CompanyView.as_view()),
    path('company/all/', views.CompanyView.as_view()),
    path('company/get/<slug:comp_slug>/', views.CompanyDetailView.as_view()),
    path('company/<int:id>/', views.CompanyDetailView.as_view()),
    path('company/<int:comp_id>/costs/', views.CompanyCostsView.as_view())
]
