from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

# local imports
from staffs.apps.authentication.serializers import (AddUserSerializer,
                                                    LoginSerializer)


class LoginUserAPIView(APIView):
    '''
    Handles user login
    '''
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        response = {
            'message': 'Login is successfully.',
            'user_data': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

class AddUserAPIView(APIView):
    '''
    Handles adding/registering new employees
    '''
    serializer_class = AddUserSerializer
    permission_classes = (IsAdminUser, )

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Employee added successfully.',
            'user_data': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
