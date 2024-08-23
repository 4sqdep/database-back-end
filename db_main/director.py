from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Categories, SubCategories, Projects
from .d_serializers import (GetCategorySerializer, GetSubCategoriesSerializer, GetChildSubCategorySerializer,
                            SearchProjectSerializer)


class GetCategoriesAPIView(APIView):
    """
    Director va Xodimlar uchun barcha kategoriyalarni olish uchun APIView
    fields = (id, user, name, created_at) GET API
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            categories = Categories.objects.all()
            serializer = GetCategorySerializer(categories, many=True)
            return Response({'message': "Barcha kategoriyalar...", 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Categories.DoesNotExist:
            return Response({'message': "Hechqanday Kategoriyalar topilmadi", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)



class GetSubCategoriesAPIView(APIView):
    """
    Kategoriyaga tekishli SubCategoriyalarni olish uchun APIView
    """

    def get(self, request, pk, format=None):
        try:
            subcategory = SubCategories.objects.filter(categories_id=pk, parent__isnull=True)
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



class SearchProjectAPIView(APIView):
    """
    Loyihalarni search qilish categoriya va subcategoriya tartiblari bilan
    fields = ['id', 'subcategory id va name' 'user id va name', 'name', 'subject', 'created_at', 'files']
    """

    def get(self, request):
        try:
            name = request.query_params.get('name')
            project = Projects.objects.filter(Q(name__icontains=name) | Q(subject__icontains=name))
            serializer = SearchProjectSerializer(project, many=True)
            return Response({'message': "Siz izlagan malumot", 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "Siz izlagan malumot topilmadi", 'data': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)