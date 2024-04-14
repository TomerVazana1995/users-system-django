from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])    
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    
    try:
        user = User.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)        

    if request.method == 'PUT':
        new_password = request.data.get('password')
        if new_password:
            user.password = new_password
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def login_user(request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')
    if email is not None and password is not None:
        try:
            user = User.objects.get(email=email, password=password)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

