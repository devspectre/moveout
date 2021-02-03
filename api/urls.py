from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

moveout_list = views.MoveoutViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

moveout_details = views.MoveoutViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('moveouts/', moveout_list, name='moveout_list'),
    path('moveouts/<int:pk>/', moveout_details, name='moveout_detail')
])