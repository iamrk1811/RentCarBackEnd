from django.urls import path, re_path, include
from account import views
from account.routers import account_router

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login-view"),
    path("register/", views.RegisterView.as_view(), name="register-view")
]

urlpatterns += account_router.urls