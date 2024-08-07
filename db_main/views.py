from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Categories, SubCategories
from .serializers import (CategoriesSerializers, SubCategoriesSerializers, SubCategoriesChildrenSerializers,
                          SubCategoriesChildrenSerializer, ProjectsSerializer, FilesSerializer, GetSubCategoriesSerializer,
                          GetCategorySerializer, GetChildSubCategorySerializer)


class CategoriesCreateAPIView(CreateAPIView):
    """
    Foydalanuvchi Obyect kategoriyalarni kiritish uchun
    """
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers

    def perform_create(self, serializer):
        if self.request.user.is_designer == True:
            serializer.save(user=self.request.user)
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


class GetSubCategoriesAPIView(APIView):
    """
    Kategoriyaga tekishli SubCategoriyalarni olish uchun APIView
    """

    def get(self, request, pk, format=None):
        try:
            subcategory = SubCategories.objects.filter(categories_id=pk, parent=None)
            print(subcategory)
            serializers = GetSubCategoriesSerializer(subcategory, many=True)
            return Response({"message": "Barcha SubCategoriyalar", 'data': serializers.data},
                            status=status.HTTP_200_OK)
        except Categories.DoesNotExist:
            return Response({'message': "Malumot topilmadi", 'data': serializers.errors},
                            status=status.HTTP_404_NOT_FOUND)


class GetChildSubCategoriesAPIView(APIView):
    """
    Ota subcategoriyaga tegishli bola kategoriyalarni olish uchun API
    """
    def get(self, request, id, format=None):
        try:
            children = SubCategories.objects.filter(parent_id=id)
            serializer = GetChildSubCategorySerializer(children, many=True)
            return Response({'message': "Bola kategoriyalar", 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except SubCategories.DoesNotExist:
            return Response({'message': "Xato....", 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)



class Children(APIView):
    """
    SubCategoriya bolalarini ko'rish uchun APIView
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        subcategories = SubCategories.objects.filter(parent__isnull=True)
        for subcategoriy in subcategories:
            print(subcategoriy.name)
        serializers = SubCategoriesChildrenSerializers(subcategories, many=True)
        return Response(serializers.data)


class CreateChildrenCreateAPIView(CreateAPIView):
    """Ota kategoriyaga bola kategoriyalarni post qilish"""
    permission_classes = [IsAuthenticated]
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesChildrenSerializer


class ProjectCreate(APIView):
    permission_classes = [IsAuthenticated],
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': "Fayllar yuklandi", 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Xatolik yuz berdi....", 'error': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)