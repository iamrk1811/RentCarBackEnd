from rest_framework.routers import DefaultRouter
from account import viewsets

account_router = DefaultRouter()

account_router.register("user", viewsets.UserViewset, basename="user-view-set")
