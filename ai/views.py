from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models.query import Q

from ai import models
from comment.models import CommentTag
# Create your views here.


def ai_main(request):
    return render(request, 'base.html')


def pool_manager(request):

    pool: models.CommentPool = models.CommentPool.objects.first()
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

