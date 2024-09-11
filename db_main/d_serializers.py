from rest_framework import serializers
from .models import Categories, SubCategories, Projects, Files
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class GetCategorySerializer(serializers.ModelSerializer):
    """
    Barcha Kategoriyalarni olish uchun serializer
    """
    class Meta:
        model = Categories
        fields = ['id', 'user', 'name', 'created_at']


class GetSubCategoriesSerializer(serializers.ModelSerializer):
    """
    Kategoriyaga tegishli SubCategoruyalarni olish uchun
    """
    children = serializers.SerializerMethodField()

    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'children']
    def get_children(self, obj):
        children = SubCategories.objects.filter(parent=obj)
        if children.exists():
            return GetSubCategoriesSerializer(children, many=True, context=self.context).data
        return []


class GetChildSubCategorySerializer(serializers.ModelSerializer):
    """
    Ota subcategoriyaga tegishli bola kategoriyalarni olish
    """
    children = serializers.SerializerMethodField()
    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'children']
    def get_children(self, obj):
        children = SubCategories.objects.filter(parent=obj)
        print("WWWWWWWWWWWW", children)
        return GetChildSubCategorySerializer(children, many=True).data


class SearchFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'file_code', 'file']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ['id', 'name']


class SearchProjectSerializer(serializers.ModelSerializer):
    files = SearchFilesSerializer(many=True, read_only=True, source='files_set')
    subcategories = SubCategorySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Projects
        fields = ['id', 'subcategories', 'user', 'name', 'subject', 'created_at', 'files']
