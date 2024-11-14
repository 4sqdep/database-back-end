from rest_framework import serializers
from .models import Categories, SubCategories, Projects, Files
from .d_serializers import UserSerializer


class  CategoriesSerializers(serializers.ModelSerializer):
    """
    Kategoriyalarni GET va POST methodlari uchun
    """
    class Meta:
        model = Categories
        fields = ('id', 'name', 'user', 'created_at')


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'created_at']


class SubCategoriesSerializers(serializers.ModelSerializer):
    """
    SubCategories Post qilish uchun
    """

    class Meta:
        model = SubCategories
        fields = ('id', 'categories', 'name')


class SubCategoriesChildrenSerializer(serializers.ModelSerializer):
    """
    SubCategories modeliga Children bolalarni biriktirish
    """
    children = serializers.ListSerializer(child=serializers.DictField(), required=False)

    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'categories', 'parent', 'children']


    def create(self, validated_data):
        children_parent = validated_data.pop('children', [])
        subcategory = SubCategories.objects.create(**validated_data)
        for child_data in children_parent:
            child_data['parent'] = subcategory
            SubCategories.objects.create(**child_data)
        return subcategory


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['file_code', 'file', 'created_at']


class ProjectsSerializer(serializers.ModelSerializer):
    files = FilesSerializer(many=True, write_only=True)
    class Meta:
        model = Projects
        fields = ['subcategories', 'name', 'subject', 'files']

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        project = Projects.objects.create(**validated_data)
        files = [Files(project=project, **file_data) for file_data in files_data]
        Files.objects.bulk_create(files, batch_size=300)
        return project


class FileSerializer(serializers.ModelSerializer):
    """
    Fayillarni olish uchun serializer
    """
    class Meta:
        model = Files
        fields = ['id', 'file_code', 'file', 'created_at']


class GetProjectSerializer(serializers.ModelSerializer):
    """
    Project va unga tegishli fayllarni olish uchun serializer
    """

    files = FilesSerializer(many=True, read_only=True, source='files_set')
    class Meta:
        model = Projects
        fields = ['id', 'name', 'subject', 'files', 'created_at']


class SearchCategorySerializer(serializers.ModelSerializer):
    """Categoriya search qilish uchun"""
    user = UserSerializer(read_only=True)
    class Meta:
        model = Categories
        fields = ['id', 'user', 'name', 'created_at']


class SubCategoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ['id', 'categories', 'name']


class ChildCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'categories', 'parent']


class GetFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['file_code', 'file', 'created_at']