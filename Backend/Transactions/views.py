from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Transactions.serializer import Transactionserializer
from rest_framework import status
from Transactions.models import Transactions
import json
from Farmer.models import Farmer
from django.db.models import Q
# Create your views here.
@api_view(['GET','POST'])
def new_transaction(request):
    if request.method == 'POST':
        data = request.POST
        # print(data)
        tr_data = {}
        
        farmer_data = Farmer.objects.filter(fm_id = data['fm_id']).first()

        if farmer_data == None:
            return Response({'message':'farmer not found'},status=status.HTTP_404_NOT_FOUND)
        
        tr_data['fm_id'] = data['fm_id']
        tr_data['fm_mobile'] = farmer_data.mobile
        tr_data['product_list'] = data['product_list']
        tr_data['total_transaction'] = data['total_transaction']
        if data['paydown'] == '':
            tr_data['paydown'] = 0
            tr_data['total_due'] = data['total_transaction']
        else:
            tr_data['paydown'] = data['paydown']
            tr_data['total_due'] = data['total_due']

        # print(tr_data)
        serializer = Transactionserializer(data = tr_data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        print("successfully_added")
        return Response({"message":"successfull"},status=status.HTTP_200_OK)
    
@api_view(['POST'])
def all_transaction(request):
    list = Transactions.objects.filter(status = 1).all()
    serializer = Transactionserializer(instance=list,many=True)
    res = json.dumps(serializer.data)
    res = {'list':res}
    return Response(res,status=status.HTTP_200_OK)

@api_view(['POST'])
def farmer_transaction(request):
    data = request.data
    id = data['id']

    list = Transactions.objects.filter(Q(status = 1) & Q(fm_id = id)) 
    serializer = Transactionserializer(instance=list,many=True)
    res = json.dumps(serializer.data)
    res = {'list':res}
    return Response(res,status=status.HTTP_200_OK)