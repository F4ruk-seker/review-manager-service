from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from comment.models import CommentModel
from comment.models import CommentTag


class StatView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        tag_list = CommentTag.objects.all()
        tag_list_dict = []

        for tag in tag_list:
            tag_list_dict.append({'name': tag.name, 'count': CommentModel.objects.filter(tag=tag).count()})

        tag_list_dict.append({'name': "unTAG", 'count': CommentModel.objects.filter(tag=None).count()})

        return Response(tag_list_dict, 200)
