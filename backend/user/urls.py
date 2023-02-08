from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('user/login/', views.login_api),
    path('user/user/', views.get_user_data),
    path('user/register/', views.register_api),
    path('user/logout/', knox_views.LogoutView.as_view()),
    path('user/logoutall/', knox_views.LogoutAllView.as_view())
]
