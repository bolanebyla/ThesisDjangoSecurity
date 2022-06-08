from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/auth/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
