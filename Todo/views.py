from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# Create your views here.

class Task_ViewSet(ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTask_ViewSet(ModelViewSet):

    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    def perform_create(self, serializer):
        serializer.save(
            task = Task.objects.get(id=self.kwargs.get('pk')),
        )

    def get_queryset(self):
        return super().get_queryset().filter(task=self.kwargs.get("pk"))