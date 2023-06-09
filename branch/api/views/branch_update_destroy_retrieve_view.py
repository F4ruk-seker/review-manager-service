from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, QuerySet
from branch.models import BranchModel
from branch.api.serializers import BranchSerializer


class BranchUpdateDestroyRetrieveView(DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'id'
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('name', 'id', 'url')
    # search_fields = ('name', 'id', 'url')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)