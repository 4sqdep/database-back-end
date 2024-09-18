from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Categories, SubCategories, Projects
from .serializers import (CategoriesSerializers, SubCategoriesSerializers, SubCategoriesChildrenSerializer,
                          ProjectsSerializer, GetCategorySerializer, GetProjectSerializer, SearchCategorySerializer)
from .permission import IsNotStaffUserPermission


class UserGetCategoriesAPIView(APIView):
    """
    Foydalanuvchi o'zi yaratgan loyiha kategoriyalarini olish uchun
    fields = (id, name, user, created_at)
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            category = Categories.objects.filter(user=user)
            serializer = GetCategorySerializer(category, many=True)
            return Response({'message': "Foydalanuvchining kategoriyalari", 'data': serializer.data},
                            status=status.HTTP_200_OK)
        except Categories.DoesNotExist:
            return Response({'message': "Foydalanuvchida kategoriya mavjut emas", 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)



class CategoriesCreateAPIView(CreateAPIView):
    """
    Foydalanuvchi Obyect kategoriyalarni kiritish uchun
    """
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            # Staff foydalanuvchilarga POST qilishni taqiqlaydi
            raise PermissionDenied(detail="Siz POST so'rovi yubora olmaysiz, chunki siz staff foydalanuvchisiz.")
        if self.request.user.is_designer == True:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied(detail="Faqat Loyihachilar toifalarni yaratishi mumkin..")


class PostProjectCreate(APIView):
    permission_classes = [IsAuthenticated, IsNotStaffUserPermission]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        #Fayllarni alohida olish
        files = request.FILES.getlist('file.file')
        user = request.user
        print('++++++++++++++++++++++++++++++++++', files)
        if not files:
            return Response({'error': 'No files were uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
        files_data = []
        for idx, file in enumerate(files):
            file_file_code = request.data.getlist('file.file_code')[idx]
            files_data.append({'file': file, 'file_code': file_file_code})
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", file_file_code, files_data)
            # if not file_file_code and file_file:
            #     return Response({'message': f"{file.file_code} {file.file} malumotlari topilmadi"},
            #                     status=status.HTTP_400_BAD_REQUEST)
            # files_data.append({'file': file_file, 'file_code': file_file_code})
        project_data = {
            'subcategories': request.data.get('subcategories'),
            'name': request.data.get('name'),
            'subject': request.data.get('subject'),
            'files': files_data
        }
        print("======================", project_data)
        serializer = ProjectsSerializer(data=project_data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'message': "Malumot qo'shildi", 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'xato': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class GetProjectAPIView(APIView):
    """
    Loyiha va unga tegishli fayillarni olish uchun
    fiels = ['id', 'name', 'subject', 'files', 'created_at'] malumotlar keladigan fildlar
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, pk):
        try:
            subcategory = SubCategories.objects.get(id=pk)
            projects = Projects.objects.filter(subcategories=subcategory).prefetch_related('files_set')
            serializer = GetProjectSerializer(projects, many=True)
            return Response({"message": "Malumotlar", "data": serializer.data},
                            status=status.HTTP_200_OK)
        except SubCategories.DoesNotExist:
            return Response({"message": "Malumot topilmadi", "error": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class SearchCategoryAPIView(APIView):
    """Kategoriya izlash uchun """
    def get(self, request):
        try:
            name = request.query_params.get('name')
            category = Categories.objects.filter(Q(name__icontains=name))
            serializer = SearchCategorySerializer(category, many=True)
            return Response({'message': "Siz izlagan malumot", 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "Siz izlagan malumot topilmadi", 'data': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


# class SubCategoriesCreateAPIView(CreateAPIView):
#     """
#     Foydalanuvchi Kategoriyalarni tanlagan holda SubCategoriya yaratish uchun CreateAPIView
#     """
#     permission_classes = [IsAuthenticated]
#     queryset = SubCategories.objects.all()
#     serializer_class = SubCategoriesSerializers
#
#     def perform_create(self, serializer):
#         if self.request.user.is_designer == True:
#             serializer.save()
#         else:
#             raise PermissionDenied(detail="Faqat Loyihachilar toifalarni yaratishi mumkin..")





# class CreateChildrenCreateAPIView(CreateAPIView):
#     """Ota kategoriyaga bola kategoriyalarni post qilish"""
#     permission_classes = [IsAuthenticated]
#     queryset = SubCategories.objects.all()
#     serializer_class = SubCategoriesChildrenSerializer