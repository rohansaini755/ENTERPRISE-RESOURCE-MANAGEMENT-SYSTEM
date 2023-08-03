from django.shortcuts import render
from .models import Branch
from .BranchSerializer import BranchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework import status
from django.db.models import Q

# Create your views here
# .

@api_view(['POST'])
def add_branch(request):
    # print(request.session.get('bid'))
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def branch_profile(request):
    bp = Branch.objects.filter(Q(bid = request.data['bid']) & Q(is_active=1)).first()
    if bp == None:
        return Response({"message" : "Not Exists"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = BranchSerializer(instance=bp)
    return Response({"data" : serializer.data},status=status.HTTP_200_OK)


@api_view(['POST'])
def get_all_branch(request):
    data = Branch.objects.filter(is_active = 1)
    serializer = BranchSerializer(instance=data,many=True)
    d = json.dumps(serializer.data)
    res = {"list":d}
    return Response(res,status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    bid = request.data['bid']
    password = request.data['password']
    
    user = Branch.objects.filter(bid = bid).first()
    # print(user.password)

    if user is None:
        res = {'message':'Branch not found'}
        res = json.dumps(res)
        return Response(res,status=status.HTTP_403_FORBIDDEN)
    
    if not user.is_active:
        return Response({'message':"Branch is Blocked"})
    
    if not user.password == password:
        res = {'message':'Incorrect Password'}
        res = json.dumps(res)
        return Response(res,status=status.HTTP_403_FORBIDDEN)
    request.session['bid'] = user.id
    request.session.set_expiry(86400)
    return Response({'message':'successfully login'})
    
@api_view(['GET', 'POST'])
def session(request):
    value = request.session.get('bid')
    print(value)
    return Response({'message': 'session successfull'})