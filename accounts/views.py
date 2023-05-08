from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class User_ViewSet(ModelViewSet):
    queryset = USER.objects.all()
    serializer_class = UserSerializer
