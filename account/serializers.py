from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializers(serializers.ModelSerializer):
    """Ro'yxatdan o'tish uchun serializers"""

    class Meta:
        model = User
        fields = ('username', 'password')


class LoginSerializers(TokenObtainPairSerializer):
    """Ro'yxatdan o'tgan foydalanuvchini tizimga kirish uchun serializers"""

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['id'] = self.user.id
        data['is_director'] = self.user.is_director
        data['is_designer'] = self.user.is_designer
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    """Foydalanuvchi profilini to'ldirish"""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']