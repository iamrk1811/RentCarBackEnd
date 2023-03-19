from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import AllowAny
from account.serializers import LoginSerializer, RegisterSerializer
from account.models import User
from account.response_schema import LoginResponseSchema
from rentcar.response_schema import DefaultBadRequestSchema
from drf_yasg.utils import swagger_auto_schema


class LoginView(APIView):
    """User login view"""
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer
    parser_classes = (JSONParser, )

    @swagger_auto_schema(
        responses={
            200: LoginResponseSchema(many=False),
            401: DefaultBadRequestSchema(many=False)
        },
        request_body=LoginSerializer(many=False)
    )
    def post(self, request):
        response = Response()
        response_data = {}
        response_serializer = None

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user)
            response_data.update({
                'refresh': str(token),
                'access': str(token.access_token),
            })
            response.status_code = status.HTTP_200_OK
            response_serializer = LoginResponseSchema(data=response_data)
        else:
            response_data["errors"] = serializer.errors
            response.status_code = status.HTTP_401_UNAUTHORIZED
            response_serializer = DefaultBadRequestSchema(data=response_data)
        response_serializer.is_valid()
        response.data = response_serializer.data
        return response


class RegisterView(APIView):
    """User register view"""
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer
    parser_classes = (JSONParser, )
    # if we change this status to False then created user will be inactive by default
    DEFAULT_IS_ACTIVE_STATUS = True

    @swagger_auto_schema(
        responses={
            200: LoginResponseSchema(many=False),
            401: DefaultBadRequestSchema(many=False)
        },
        request_body=RegisterSerializer(many=False)
    )
    def post(self, request):
        response = Response()
        response_data = {}
        response_serializer = None

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.data, is_active=self.DEFAULT_IS_ACTIVE_STATUS)
            token = RefreshToken.for_user(user)
            response_data.update({
                'refresh': str(token),
                'access': str(token.access_token),
            })
            response.status_code = status.HTTP_201_CREATED
            response_serializer = LoginResponseSchema(data=response_data)
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            response_data["errors"] = serializer.errors
            response_serializer = DefaultBadRequestSchema(data=response_data)
        response_serializer.is_valid()
        response.data = response_serializer.data
        return response
