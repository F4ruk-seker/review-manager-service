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


class PoolOutput(View):

    def get(self, request, pool_id, *args, **kwargs):
        pool: models.CommentPool = get_object_or_404(models.CommentPool, id=pool_id)
        output_file_name: str = generate_output_file_name(pool.id, '', 'pool')
        return render(request, 'download_modal.html', context={
            'output_file_name': output_file_name
        })

    def post(self, request, pool_id, *args, **kwargs):
        pool: models.CommentPool = get_object_or_404(models.CommentPool, id=pool_id)
        comment_list: list = pool.comments.all()

        file_type: str = request.POST.get('file_type')

        file_type_functions: dict = {
            'json': output_functions.get_rendered_json_file_response,
            'excel': output_functions.get_rendered_excel_file_response,
            'xml': output_functions.get_rendered_xml_file_response,
        }
        if render_func := file_type_functions.get(file_type):
            return render_func(pool, comment_list)
        else:
            raise Http404
