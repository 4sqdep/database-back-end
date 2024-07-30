from rest_framework import serializers
from .models import Categories, SubCategories


class CategoriesSerializers(serializers.ModelSerializer):
    """
    Kategoriyalarni GET va POST methodlari uchun
    """
    class Meta:
        model = Categories
        fields = ('id', 'name', 'user')


class SubCategoriesSerializers(serializers.ModelSerializer):
    """
    SubCategories Post qilish uchun
    """

    class Meta:
        model = SubCategories
        fields = ('id', 'categories', 'name')


class SubCategoriesChildrenSerializers(serializers.ModelSerializer):
    """
    Bolalarini olish uchun serializers
    """
    children = serializers.SerializerMethodField()

    class Meta:
        model = SubCategories
        fields = ['id', 'name', 'categories', 'parent', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return SubCategoriesChildrenSerializers(children, many=True)



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
