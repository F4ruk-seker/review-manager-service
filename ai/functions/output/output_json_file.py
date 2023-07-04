from django.shortcuts import HttpResponse
from ai.models import CommentPool
from ai.functions.output.output_file_name import generate_output_file_name
from comment.models import CommentModel
import json


def get_rendered_json_file_response(pool: CommentPool, comment_list: list[CommentModel]) -> HttpResponse:
    # output: list = [json.dumps(comment.get_as_json()) for comment in comment_list]
    output: list = [comment.get_as_json() for comment in comment_list]
    output_file_name: str = generate_output_file_name(pool.id, "json")
    response = HttpResponse(json.dumps(output), content_type='application/vnd.ms-json')
    response['Content-Disposition'] = f'attachment; filename={output_file_name}'
    return response

