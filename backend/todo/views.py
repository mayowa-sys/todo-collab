from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoViewsets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)