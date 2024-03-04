from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github", views.login_github, name="login_github"),
    path("login/github/callback/", views.login_github_callback, name="login_github_callback"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.log_out, name="logout"),
]
