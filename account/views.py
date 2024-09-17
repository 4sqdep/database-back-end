from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterSerializers, LoginSerializers, UserProfileSerializer


class RegistrationAPIView(APIView):
    """Foydalanuvchini tizimga kirish uchun ro'yxatdan o'tkazish"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Malumot kiritilmadi", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()
        return Response({'message': "Foydalanuvchi ro'yxatdan o'tkazildi"},
                        status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    """
    Foydalanuvchi tizimga kirish uchun
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializers

user_login_api_view = LoginView().as_view()


class UserProfileAPIView(APIView):
    """Foydalanuvchi profilini yaratish va yangilash
        fields = ['id', 'first_name', 'last_name']
    """
    def get(self, request, pk=None):
        userprofile = User.objects.get(id=pk)
        serializer = UserProfileSerializer(userprofile)
        return Response({'message': 'Foydalanuvchi profili', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        try:
            profile = User.objects.get(id=pk)
            serializer = UserProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': "Profile toldirildi!", 'data': serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': "Foydalanuvchi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        try:
            profile = User.objects.get(id=pk)
            serializer = UserProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': "Profil o'zgartirildi", 'data': serializer.data}, status=status.HTTP_200_OK)
            return Response({'message': "Xatolik yuzberdi", 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': "Foydalanuvchi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)