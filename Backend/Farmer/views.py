from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Farmer.serializer import Farmerserializer
from rest_framework import status
from Farmer.models import Farmer
import json
# Create your views here.


@api_view(['GET'])
def check(request):
    return Response({"message":"successfull"})

@api_view(['GET','POST'])
def new_farmer(request):
    data = request.data
    print(data)
    farmer_data = {}
    farmer_data['first_name'] = data['fname']
    farmer_data['middle_name'] = data['mname']
    farmer_data['last_name'] = data['lname']
    farmer_data['father_name'] = data['fathername']
    farmer_data['gender'] = data['gender']
    farmer_data['address'] = data['address']
    farmer_data['mobile'] = data['mobile']
    farmer_data['whatsapp_mobile'] = data['whatsappmobile']
    serializer = Farmerserializer(data = farmer_data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response({"message":"successfull"},status=status.HTTP_200_OK)

# @api_view(['POST'])
# def get_all_farmer(request):
#     list = Farmer.objects.all()
#     list = Farmerserializer(data=list)
#     res = json.dumps(list.data)
#     res = {"list":res}
#     return Response(res,status=status.HTTP_200_OK)

# @api_view(['POST'])
# def get_all_farmer(request):
#     queryset = Farmer.objects.all()
#     serializer = Farmerserializer(data=queryset, many=True)
#     serializer.is_valid(raise_exception=True)
#     res = json.dumps(serializer.data)
#     res = {"list": res}
#     return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_all_farmer(request):
    queryset = Farmer.objects.filter(status=1)
    serializer = Farmerserializer(instance=queryset, many=True)
    res = json.dumps(serializer.data)
    res = {"list": res}
    return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def farmer_profile(request):
    id = request.data['id']
    print(id)
    data = Farmer.objects.filter(fm_id = id).first()
    
    if data == None:
        return Response({"error:Not Found"},status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = Farmerserializer(instance=data)
        res = json.dumps(serializer.data)
        res = {'data':res}
        return Response(res,status=status.HTTP_200_OK)


