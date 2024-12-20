from django.urls import path
from .views import (CategoriesCreateAPIView, UserGetCategoriesAPIView, PostProjectCreate, GetProjectAPIView,
                    SearchCategoryAPIView, SearchSubCategoryAPIView, AddSubCategoryAPIView, AddChildAPIView,
                    GetPrpjectFilesAPIView)
from .director import GetCategoriesAPIView, GetSubCategoriesAPIView, SearchProjectAPIView


app_name = "db_main"

urlpatterns = [
    path('categories-create/', CategoriesCreateAPIView.as_view(), name="categories-create"),
    path('user-category/', UserGetCategoriesAPIView.as_view(), name='user-category'),
#    DIRECTOR UCHUN
    path('category-all/', GetCategoriesAPIView.as_view(), name='category-all'),
    path('get-subcategories/<int:pk>/', GetSubCategoriesAPIView.as_view(), name='get-subcategories'),
    path('post-project/', PostProjectCreate.as_view(), name='post-project'),
    path('get-project/<int:pk>/', GetProjectAPIView.as_view(), name='get-project'),
    path('search-project/<int:pk>/', SearchProjectAPIView.as_view(), name='search-project'),
    path('add-subcategory/<int:pk>/', AddSubCategoryAPIView.as_view(), name='add-subcategory'),
    path('add-child/<int:pk>/', AddChildAPIView.as_view(), name='add-child'),

    path('category-search/', SearchCategoryAPIView.as_view(), name='category-search'),

    path('subcategory-search/<int:pk>/', SearchSubCategoryAPIView.as_view(), name='subcategory-search'),

    path('get-files/<int:pk>/', GetPrpjectFilesAPIView.as_view(), name='get-files')
]