from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeView.as_view()),
    path('employees/<int:comp_id>/', views.EmployeeView.as_view())
]
