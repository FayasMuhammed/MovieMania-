from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from api.serializers import Movie_model,Genre_model,Movie_serializer,Genre_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication,permissions



class Genre_viewset(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Genre_model.objects.all()
        serializer=Genre_serializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Genre_model.objects.get(id=id)
        serializer=Genre_serializer(qs)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request,*args,**kwargs):
        serializer=Genre_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Genre_model.objects.get(id=id)
        serializer=Genre_serializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Genre_model.objects.get(id=id).delete()
        return Response({"success":"deleted"},status=status.HTTP_200_OK)        
    

class Movie_viewset(ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Movie_model.objects.all()
        serializer=Movie_serializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie_model.objects.get(id=id)
        serializer=Movie_serializer(qs)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request,*args,**kwargs):
        serializer=Movie_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie_model.objects.get(id=id)
        serializer=Movie_serializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie_model.objects.get(id=id).delete()
        return Response({"deleted":"successfully"},status=status.HTTP_200_OK)


