from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Farmer.serializer import Farmerserializer
from rest_framework import status
from Farmer.models import Farmer
from Associated_company.models import Company
from Associated_company.serializer import Companyserializer
import json
# Create your views here.



@api_view(['POST'])
def new_company(request):
    data = request.data
    print(data)
    company_data = {}
    count = Company.objects.all().count()
    cmp = Company.objects.filter(mobile = data['phone'])
    if cmp:
        return Response({"message" : "mobile number is already registered"},status=status.HTTP_306_RESERVED)
    # print(data)
    cmp_code = "2022" + str(count+1)
    company_data['cmp_code'] = cmp_code
    company_data['company_name'] = data['cname']
    company_data['ceo_name'] = data['ceoname']
    company_data['address'] = data['address']
    company_data['mobile'] = data['phone']
    company_data['company_type'] = data['type']
    company_data['whatsapp_mobile'] = data['address']
    company_data['dealer_name'] = data['dealer_name']
    company_data['dealer_address'] = data['dealer_address']
    company_data['dealer_mobile'] = data['dealer_mobile_no']
    company_data['dealer_whatsapp'] = data['dealer_whatsapp_no']
    company_data['email'] = data['email']
    serializer = Companyserializer(data = company_data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    res = {"message" : "success"}
    return Response(res,status=status.HTTP_200_OK)

@api_view(['POST'])
def get_all_company(request):
    queryset = Company.objects.filter(status=1)
    serializer = Companyserializer(instance=queryset, many=True)
    res = json.dumps(serializer.data)
    res = {"list": res}
    return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def company_detail(request):
    id = request.data['id']
    queryset = Company.objects.filter(cmp_id=id).first()
    serializer = Companyserializer(instance=queryset)
    res = json.dumps(serializer.data)
    res = {"data": res}
    return Response(res, status=status.HTTP_200_OK)

