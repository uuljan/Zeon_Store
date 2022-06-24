from rest_framework.serializers import ModelSerializer, \
    CharField, ValidationError, EmailField, Serializer
from django.contrib.auth import authenticate

from .models import User

import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCWHefQX_9iPKF2C6kEPbPSieGvxlMSN64",
    "authDomain": "authe-53baf.firebaseapp.com",
    "projectId": "authe-53baf",
    "storageBucket": "authe-53baf.appspot.com",
    "messagingSenderId": "795809514644",
    "appId": "1:795809514644:web:12ae7b0f03d5c4ac48e081",
    "measurementId": "G-Q6HRK1JVDE",
    "databaseURL": "https://authe-53baf-default-rtdb.firebaseio.com",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class RegistrationSerializer(ModelSerializer):
    """Сериализатор для регистрации"""
    email = User.email
    password = CharField(max_length=10)
    password_confirm = CharField(max_length=10)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.pop('password_confirm')
        if password != password_confirm:
            msg = ('Пароли не совпадают')
            raise ValidationError(msg)
        return data

    def create(self, validated_data):
        user = auth.create_user_with_email_and_password(**validated_data)
        return user


class LoginSerializer(Serializer):
    """Сериализатор для login"""

    email = EmailField(required=True)
    password = CharField(required=True)

    # def validate_email(self, email):
    #     user = User.objects.filter(email=email).exists()
    #     if not user:
    #         msg = ('Пользователь не найден')
    #         raise ValidationError(msg)
    #     return email

    def validate(self, data):
        request = self.context.get('request')
        email = data.get('email')
        password = data.get('password')
        # user = authenticate(
        #     request,
        #     email=email,
        #     password=password,
        # )
        user = auth.sign_in_with_email_and_password(email, password)

        if not user:
            msg = ('Данные не верны')
            raise ValidationError(msg)
        data['user'] = user
        return data
