from django.urls import path

from vendor.views import ProductGeneric, ProductGenericCategoryView, CategoryGeneric, ImageGeneric, \
    ImageGenericProductView

app_name = "vendor"
urlpatterns = [
    path('product/', ProductGeneric.as_view(), name='Product'),
    path('product/<int:pk>', ProductGenericCategoryView.as_view(), name='Product-category'),
    path('image/<int:pk>', ImageGenericProductView.as_view(), name='Product-category'),
    path('category/', CategoryGeneric.as_view(), name='category'),
    path('image/', ImageGeneric.as_view(), name='image'),
]
