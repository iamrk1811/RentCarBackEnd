from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserViewset(ViewSet):
    permission_classes = (IsAuthenticated, )

    @action(methods=["POST"], detail=False, url_path="user-profile")
    def user_profile(self, request):
        pass
        return Response("okay")


