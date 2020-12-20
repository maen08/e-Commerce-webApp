from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from Cart.serializers import ProductSerializer

def home_view(request):
    return render(request, template_name='category-full.html')


def product_list(request):
    product_list = Product.objects.all()
    
    args = {
        'product_list':product_list
    }

    return render(request, template_name='base.html', context=args)

def detail_view(request, product_id):
    detail = Product.objects.filter(pk=product_id)
    args = {
        'detail':detail
    }
    return render(request, template_name='detail2.html', context=args)



class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer