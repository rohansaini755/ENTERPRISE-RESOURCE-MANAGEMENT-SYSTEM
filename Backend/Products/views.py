from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Products.serializer import Productserializer,TemplateSerializer
from rest_framework import status
from Products.models import Product,Templates
import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['POST'])
def new_template(request):
    data = request.data
    print(data)
    serializer = TemplateSerializer(data = data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def get_all_template(request):
    data = Templates.objects.filter(status=1)
    serializer = TemplateSerializer(instance=data, many=True)
    template_list = []
    for data_item in serializer.data:
        d = {}
        d['tmp_id'] = data_item['tmp_id']
        d['tmp_name'] = data_item['tmp_name']
        d['tmp_description'] = data_item['tmp_description']
        product_list = []
        for i in range(1, 11):
            product_key = f'tmp_pr_{i}'
            product_id = data_item[product_key]
            if product_id is not None:
                product = get_object_or_404(Product, pk=product_id)
                product_data = {
                    'id': product.pk,
                    'name': product.pr_name,
                    'detail': product.pr_detail,
                    'price': product.pr_price,
                }
                product_list.append(product_data)

        d['products'] = product_list
        template_list.append(d)

    data = {"list": template_list}
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def new_product(request):
    data = request.data
    print(data)
    info = {}
    info['pr_company'] = data['pr_company']
    info['pr_name'] = data['pr_name']
    info['pr_salt'] = data['pr_salt']
    info['pr_detail'] = data['pr_detail']
    info['pr_instructions'] = data['pr_instructions']
    info['pr_type'] = data['pr_type']
    info['pr_price'] = data['pr_price']
    info['status'] = 1
    pr = Product.objects.filter(pr_name = data['pr_name']).first()
    # print(pr.pr_name)
    # print(pr.status)
    if pr != None and pr.status == 1:
        return Response({"message": "Product is already exists"})
    serializer = Productserializer(data = info)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response({"message":"successfull"},status=status.HTTP_200_OK)

@api_view(['POST'])
def get_all_product(request):
    queryset = Product.objects.filter(status=1)
    serializer = Productserializer(instance=queryset, many=True)
    res = json.dumps(serializer.data)
    res = {"list": res}
    return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def product_list(request):
    print(request.data['pr_company'])
    queryset = Product.objects.filter(Q(status = 1) & Q(pr_company = request.data['pr_company']))
    if queryset is None:
        return Response({"message":"Data not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = Productserializer(instance = queryset,many=True)
    res = json.dumps(serializer.data)
    res = {"list":res}
    return Response(res,status=status.HTTP_200_OK)