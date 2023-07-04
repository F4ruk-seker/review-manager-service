from rest_framework.generics import ListAPIView, RetrieveAPIView

from ai.api.serializers import PoolCommentSerializer
from ai.models import CommentPool


class PoolCommentList(RetrieveAPIView):
    queryset = CommentPool.objects.all()
    serializer_class = PoolCommentSerializer

    lookup_field = 'pk'

