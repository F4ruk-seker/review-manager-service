from django.views.generic import TemplateView
from comment.api.serializers import CommentTagSerializer
from comment.models import CommentTag

import json


class PoolFastTagView(TemplateView):
    template_name = 'fast_tag.html'

    @staticmethod
    def get_tags() :
        comments: list[CommentTag] = CommentTag.objects.all()
        return [CommentTagSerializer(comment).data for comment in comments]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags']: list = self.get_tags()
        return context
