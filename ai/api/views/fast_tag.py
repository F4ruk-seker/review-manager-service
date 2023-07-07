from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

from ai.api.serializers import CommentTagSerializer
from comment.models import CommentModel


class FastTagPagination(PageNumberPagination):
    page_size = 1


class FastTag(ListCreateAPIView):
    pagination_class = FastTagPagination
    serializer_class = CommentTagSerializer
    queryset = CommentModel.objects.filter(tag=None).order_by('id')

