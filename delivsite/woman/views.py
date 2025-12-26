# from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics

# from .serializer import WomanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Woman
from .serializer import WomanSerializer

class WomanAPIList(generics.ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    
class WomanAPIView(APIView):
    
    def get(self, request):
        w =Woman.objects.all()
        return Response({'posts':WomanSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # post_new = Woman.objects.create(
        #     title = request.data['title'],
        #     content =request.data['content'],
        #     cat_id = request.data['cat_id']
        # )
        serializer.save()
        return Response({'post':serializer.data})
    
    def put(self,request,*args,**kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"error":"Method PUT not allowed"})
        try:
            instance =Woman.objects.get(pk=pk)
        except:
            return Response({"error":"Object doesn't exists"})
        serializer = WomanSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})
    
    def delete(self,request,*args,**kwargs):
        pk=kwargs.get("pk",None)
        if not pk:
            return Response({"error":"Method DELETE not allowed"})
        return Response({"post":"delete post" + str(pk)})
    
# Create your views here.
# class WomanAPIView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer