from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Get all products or create a new one
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        print("raw data: ", serializer.initial_data)
        if serializer.is_valid():
            print("validate_data: ", serializer.validated_data)
            serializer.save()
            print("serializer instance type after saved: ", type(serializer.instance))
            print("serializer instance data after saved: ", serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

