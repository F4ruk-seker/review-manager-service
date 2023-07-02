from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from comment.models import CommentTag
from comment.api.serializers import CommentTagSerializer


class CommentTagListView(ListAPIView):
    queryset = CommentTag.objects.all()
    serializer_class = CommentTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('text', 'id', 'branch_from', 'ai_tag', 'tag')
    search_fields = ('text', 'id', 'branch_from', 'ai_tag', 'tag')



