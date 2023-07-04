from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from ai.models import CommentPool
from comment.models import CommentModel
from comment.api.serializers import CommentSerializer
from ai.api.serializers import PoolCommentSerializer, PoolSerializer


class PoolListSearchView(ListAPIView):

    queryset = CommentPool.objects.all()
    serializer_class = PoolSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('name', 'id', 'url')
    # search_fields = ('name', 'id', 'url')
