from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

from .models import Moveout
from .serializers import MoveoutSerializer
from .utils import EnablePartialUpdateMixin

# Create your views here.
class MoveoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows moveouts to be viewed or edited
    """
    queryset = Moveout.objects.all().order_by('-date')
    serializer_class = MoveoutSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)