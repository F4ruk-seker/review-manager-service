from django.http import Http404
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from ai import models
from ai.functions import output as output_functions
# from ai.functions.output import generate_output_file_name


class PoolOutput(View):

    def get(self, request, pool_id, *args, **kwargs):
        pool: models.CommentPool = get_object_or_404(models.CommentPool, id=pool_id)
        output_file_name: str = output_functions.generate_output_file_name(pool.id, '', 'pool')
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
