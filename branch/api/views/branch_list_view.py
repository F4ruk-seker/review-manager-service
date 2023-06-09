from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status
from branch.models import BranchModel
from branch.api.serializers import BranchSerializer


class BranchSearchListView(ListAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'id', 'url')
    search_fields = ('name', 'id', 'url')

