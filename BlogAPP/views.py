from django.shortcuts import render, redirect
from django.utils import timezone
from .models import blogs
from .serializers import blogserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def home(request):
    return render (request, 'home.html')

@api_view(['GET'])
def viewblog(request):
    if request.method == 'GET':
        blogdata=blogs.objects.all()
        serial=blogserializers(blogdata, many=True)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    else: 
        return Response (status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addblog(request):
    if request.method=='POST':
        blogdata=blogserializers(data=request.data)
        if blogdata.is_valid():
            blogdata.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)
        
def delete(request):
    if request.method=='GET':
        blogdata=blogs.objects.all()
        serial=blogserializers(blogdata, many=True)
        return render (request, 'delete.html', {'blogdata':serial.data})
    else:
        return Response (status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE', 'GET'])
def deleteid(request, id):
    try:
        blogid=blogs.objects.get(id=id)
    except blogs.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=blogserializers(blogid)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        blogs.delete(blogid)
        return Response(status=status.HTTP_202_ACCEPTED)

def edit(request):
    if request.method=='GET':
        blogdata=blogs.objects.all()
        serial=blogserializers(blogdata, many=True)
        return render (request, 'update.html', {'blogdata':serial.data})
    else:
        return Response (status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET'])
def editid(request, id):
    try:
        blogid = blogs.objects.get(id=id)
    except blogs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = blogserializers(blogid)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['updated'] = timezone.now()
        
        serializerdata = blogserializers(data=request.data, instance=blogid)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getid(request,id):
    try:
        blogid=blogs.objects.get(id=id)
    except blogs.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    serial=blogserializers(blogid)
    return Response (data=serial.data, status=status.HTTP_200_OK)
