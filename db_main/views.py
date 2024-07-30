from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from .models import Categories, SubCategories
from .serializers import (CategoriesSerializers, SubCategoriesSerializers, SubCategoriesChildrenSerializers,
                          SubCategoriesChildrenSerializer)


class CategoriesCreateAPIView(CreateAPIView):
    """
    Foydalanuvchi Obyect kategoriyalarni kiritish uchun
    """
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers

    def perform_create(self, serializer):
        if not self.request.user.is_designer == True:
            serializer.validated_data['user']
            serializer.save()
        else:
            raise PermissionDenied(detail="Faqat Loyihachilar toifalarni yaratishi mumkin..")


class SubCategoriesCreateAPIView(CreateAPIView):
    """
    Foydalanuvchi Kategoriyalarni tanlagan holda SubCategoriya yaratish uchun CreateAPIView
    """
    permission_classes = [IsAuthenticated]
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializers

    def perform_create(self, serializer):
        if self.request.user.is_designer == True:
            serializer.save()
        else:
            raise PermissionDenied(detail="Faqat Loyihachilar toifalarni yaratishi mumkin..")


class Children(APIView):
    """
    SubCategoriya bolalarini ko'rish uchun APIView
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        subcategories = SubCategories.filter(parent__isnull=True)
        serializers = SubCategoriesChildrenSerializers(subcategories, many=True)
        return Response(serializers.data)


class CreateChildrenCreateAPIView(CreateAPIView):
    """Ota kategoriyaga bola kategoriyalarni post qilish"""
    permission_classes = [IsAuthenticated]
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesChildrenSerializer


