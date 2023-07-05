from .pool_output import PoolOutput
from .pool_list_view import PoolView
from comment.api.serializers import CustomizedCommentBranchSerializer

from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.db.models.query import Q
from django.views.generic import View

from ai import models
from comment.models import CommentTag

# Create your views here.


from ai.functions import output as output_functions
from ai.functions.output import generate_output_file_name

def ai_main(request):
    return render(request, 'base.html')


class PoolManager(DetailView):
    queryset = models.CommentPool.objects.all()
    pk_url_kwarg = 'pool_id'
    template_name = 'pool_manager.html'
    context_object_name = 'pool'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.request.GET.get('tag', None)
        comments = self.object.comments.all()

        if tag:
            if tag == 'unTAG':
                comments = self.object.comments.filter(tag=None)
            else:
                tag = get_object_or_404(CommentTag, name=tag)
                comments = self.object.comments.filter(Q(tag=tag))
        context['comments'] = [CustomizedCommentBranchSerializer(comment).data for comment in comments]
        return context

def pool_manager(request, pool_id):

    pool: models.CommentPool = models.CommentPool.objects.filter(id=pool_id).first()
    tag = request.GET.get('tag', None)
    ai = request.GET.get('ai', None)
    comment = pool.comments.all()

    if tag:
        if tag == 'unTAG':
            comment = pool.comments.all().filter(tag=None)
        else:
            tag: CommentTag = get_object_or_404(CommentTag, name=tag)
            query = (Q(ai_tag=tag) | (Q(tag=tag))) if ai == 'true' else (Q(tag=tag))
            comment = pool.comments.filter(query)

    return render(request, 'pool_manager.html', context={
        'pool': pool,
        'comments': comment
    })


