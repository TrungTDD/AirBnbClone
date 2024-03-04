import requests
import os
from http import HTTPStatus
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, authenticate, logout

from . import forms
from .models import User

# Create your views here


# class LoginView(View):
#     def get(self, request):
#         form = forms.LoginForm()
#         return render(request, "users/login.html", context={"form": form})

#     def post(self, request):
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             return redirect(reverse("core:home"))
#         else:
#             return render(request, "users/login.html", context={"form": form})


def _login(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)


class LoginView(FormView):
    template_name = "users/login.html"
    success_url = reverse_lazy("core:home")
    form_class = forms.LoginForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        _login(self.request, username, password)
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = "users/register.html"
    success_url = reverse_lazy("core:home")
    form_class = forms.RegisterForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        _login(self.request, username, password)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


def login_github(request):
    client_id = os.environ.get("GITHUB_CLIENT_ID")
    return redirect(
        f"https://github.com/login/oauth/authorize?scope=read:user&client_id={client_id}"
    )


def login_github_callback(request):
    code = request.GET.get("code")
    if not code:
        return redirect(reverse("core:home"))
    client_id = os.environ.get("GITHUB_CLIENT_ID")
    client_secret = os.environ.get("GITHUB_CLIENT_SECRET")
    token_request = requests.post(
        f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
        headers={
            "Accept": "application/json",
        },
    )
    if token_request.status_code == HTTPStatus.OK:
        token_response = token_request.json()
        access_token = token_response.get("access_token", None)
        if not access_token:
            return redirect(reverse("core:home"))
        auth_request = requests.get(
            "https://api.github.com/user",
            headers={
                "Accept": "application/json",
                "Authorization": f"bearer {access_token}"
            },
        )

        if auth_request.status_code == HTTPStatus.OK:
            auth_response = auth_request.json()
            name = auth_response.get("login", None)
            try:
                print("Log in via github")
                user = User.objects.get(username=name, login_method=User.GITHUB_LOGIN)
            except User.DoesNotExist:
                print("Create new account and Log in via github")
                user = User.objects.create(username=name, login_method=User.GITHUB_LOGIN)
                user.set_unusable_password()
                user.save()
            login(request, user)
            return redirect(reverse("core:home"))
        else:
            return redirect(reverse("core:home"))
    else:
        return redirect(reverse("core:home"))
