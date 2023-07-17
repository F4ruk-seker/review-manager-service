from django.utils import timezone

from django.views.generic import View
from rest_framework.generics import UpdateAPIView, get_object_or_404, GenericAPIView
from rest_framework.response import Response
from comment.models import CommentModel
from comment.api.serializers import CommentSerializer, CommentPassSerializer


class CommentPass(GenericAPIView):
    queryset = CommentModel
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        comment = kwargs.get('id', None)
        comment = get_object_or_404(CommentModel, id=comment)  # Retrieve the comment instance
        comment.pass_time_out = timezone.now() + timezone.timedelta(hours=24)
        comment.save()

        return Response(CommentSerializer(initial=comment).data)
