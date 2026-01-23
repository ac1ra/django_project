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
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class WomanAPIList(generics.ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class WomanAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
class WomanAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAdminOrReadOnly,)
