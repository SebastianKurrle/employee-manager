from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeView.as_view()),
    path('employee/<int:comp_id>/<int:emp_id>/', views.EmployeeDetailView.as_view()),
    path('employees/<int:comp_id>/', views.EmployeeView.as_view())
]
