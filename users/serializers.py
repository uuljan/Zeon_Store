from rest_framework.serializers import ModelSerializer, \
    CharField, ValidationError, EmailField, Serializer
from django.contrib.auth import authenticate

from .models import User


class RegistrationSerializer(ModelSerializer):
    """Сериализатор для регистрации"""

    password = CharField(max_length=4)
    password_confirm = CharField(max_length=4)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm', 'username')

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.pop('password_confirm')
        if password != password_confirm:
            msg = ('Пароли не совпадают')
            raise ValidationError(msg)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(Serializer):
    """Сериализатор для login"""

    email = EmailField(required=True)
    password = CharField(required=True)
    username = CharField(required=True)

    def validate_email(self, email):
        user = User.objects.filter(email=email).exists()
        if not user:
            msg = ('Пользователь не найден')
            raise ValidationError(msg)
        return email

    def validate(self, data):
        request = self.context.get('request')
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')
        user = authenticate(
            request,
            email=email,
            password=password,
            username=username
        )

        if not user:
            msg = ('Данные не верны')
            raise ValidationError(msg)
        data['user'] = user
        return data
