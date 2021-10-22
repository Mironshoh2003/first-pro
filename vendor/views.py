from rest_framework import viewsets, generics
from rest_framework import permissions
from vendor.models import Product, Category, ProductImage
from vendor.serializers import ProductSerializer, CategorySerializer, ImageSerializer


class ProductGeneric(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageGeneric(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ImageSerializer


class ProductGenericCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        pk = self.kwargs['pk']
        return Product.objects.filter(category__id=pk)


class ImageGenericProductView(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        pk = self.kwargs['pk']
        return ProductImage.objects.filter(product__id=pk)


class CategoryGeneric(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
