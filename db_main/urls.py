from django.urls import path
from .views import (CategoriesCreateAPIView, SubCategoriesCreateAPIView, Children, CreateChildrenCreateAPIView,
                    GetSubCategoriesAPIView, GetChildSubCategoriesAPIView)


app_name = "db_main"

urlpatterns = [
    path('categories-create/', CategoriesCreateAPIView.as_view(), name="categories-create"),
    path('`subcategories-create/`', SubCategoriesCreateAPIView.as_view(), name='subcategories-create'),
    path('children/', Children.as_view(), name='children'),
    path('children-post/', CreateChildrenCreateAPIView.as_view(), name='children-post'),
    path('get-subcategories/<int:pk>/', GetSubCategoriesAPIView.as_view(), name='get-subcategories'),
    path('get-children/<int:id>/', GetChildSubCategoriesAPIView.as_view(), name='get-children')
]