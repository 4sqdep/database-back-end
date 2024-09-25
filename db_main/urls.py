from django.urls import path
from .views import (CategoriesCreateAPIView, UserGetCategoriesAPIView, PostProjectCreate, GetProjectAPIView,
                    SearchCategoryAPIView, SearchSubCategoryAPIView)
from .director import GetCategoriesAPIView, GetSubCategoriesAPIView, GetChildSubCategoriesAPIView, SearchProjectAPIView


app_name = "db_main"

urlpatterns = [
    path('categories-create/', CategoriesCreateAPIView.as_view(), name="categories-create"),
    path('user-category/', UserGetCategoriesAPIView.as_view(), name='user-category'),
    # path('`subcategories-create/`', SubCategoriesCreateAPIView.as_view(), name='subcategories-create'),
    # path('children-post/', CreateChildrenCreateAPIView.as_view(), name='children-post'),
#     DIRECTOR UCHUN
    path('category-all/', GetCategoriesAPIView.as_view(), name='category-all'),
    path('get-subcategories/<int:pk>/', GetSubCategoriesAPIView.as_view(), name='get-subcategories'),
    # path('get-children/<int:id>/', GetChildSubCategoriesAPIView.as_view(), name='get-children'),
    path('post-project/', PostProjectCreate.as_view(), name='post-project'),
    path('get-project/<int:pk>/', GetProjectAPIView.as_view(), name='get-project'),
    path('search-project/<int:pk>/', SearchProjectAPIView.as_view(), name='search-project'),

    path('category-search/', SearchCategoryAPIView.as_view(), name='category-search'),

    path('subcategory-search/<int:pk>/', SearchSubCategoryAPIView.as_view(), name='subcategory-search')
]