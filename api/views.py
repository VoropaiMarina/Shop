import shop.main.models

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import NotebookSerializer
from shop.main.models import Notebook


class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all().order_by('display_type')
    serializer_class = NotebookSerializer
