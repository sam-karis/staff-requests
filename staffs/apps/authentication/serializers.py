from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed

# local imports
from staffs.apps.authentication.models import User, Role


class LoginSerializer(serializers.Serializer):
    """
    Serializer to validate credentials during login
    """
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=500, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)

        if user is None:
            raise AuthenticationFailed(
                'Invalid email or password', status.HTTP_401_UNAUTHORIZED)

        user_detail = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'access_token': user.token
        }
        return user_detail


class AddUserSerializer(serializers.ModelSerializer):
    """
    Serializer to validate employees details
    """

    def validate(self, data):
        confirm_password = data.get('confirm_password', None)
        if data['password'] != confirm_password:
            raise serializers.ValidationError(
                {"Password": "Password and confirm password don't match."}
            )
        return data

    confirm_password = serializers.CharField(
        max_length=60, required=True, write_only=True)
    password = serializers.CharField(
        max_length=60, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'line_manager', 'role', 'created_at', 'updated_at',
                  'password', 'confirm_password']
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        # Use the `create_user` create a new user.
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(**validated_data)


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer to validate role details
    """
    class Meta:
        model = Role
        fields = ['name', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')
