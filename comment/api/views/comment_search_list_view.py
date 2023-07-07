from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status
from comment.models import CommentModel
from comment.api.serializers import CustomizedCommentBranchSerializer


class CommentSearchListView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CustomizedCommentBranchSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('text', 'id', 'branch_from', 'ai_tag', 'tag')
    search_fields = ('text', 'id', 'branch_from', 'ai_tag', 'tag')


