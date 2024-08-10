from rest_framework import serializers
from .models import Categories, SubCategories



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
    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'parent']


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