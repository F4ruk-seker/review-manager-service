from django.utils import timezone

from django.views.generic import View
from rest_framework.generics import UpdateAPIView, get_object_or_404, GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from comment.models import CommentModel
from comment.api.serializers import CommentSerializer, CommentPassSerializer


class CommentPass(GenericAPIView):
    queryset = CommentModel
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        if comment := kwargs.get('id', None):
            comment = get_object_or_404(CommentModel, id=comment)  # Retrieve the comment instance
            comment.pass_time_out = timezone.now() + timezone.timedelta(hours=24)
            comment.save()

            response = Response(CommentSerializer(initial=comment).data)
            # response.accepted_renderer = JSONRenderer()
            # response.accepted_media_type = 'application/json'  # Set the appropriate media type
            #
            return response
