# from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics,viewsets,mixins
from rest_framework.decorators import action
# from .serializer import WomanSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Woman, Category
from .serializer import WomanSerializer

# class WomanViewSet(viewsets.ModelViewSet):
# class WomanViewSet(viewsets.ReadOnlyModelViewSet):
class WomanViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                #    mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet
                   ):
   #  queryset =Woman.objects.all()
    serializer_class=WomanSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
           return Woman.objects.all()[:3]
        return Woman.objects.filter(pk=pk)
    @action(methods=['get'],detail=True)
    def category(self,request,pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

# class WomanAPIList(generics.ListCreateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
    

# class WomanAPIUpdate(generics.UpdateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer

# class WomanAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
