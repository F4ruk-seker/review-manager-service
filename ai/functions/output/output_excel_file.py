from .output_file_name import generate_output_file_name

from ai.models import CommentPool
from comment.models import CommentModel
from django.shortcuts import HttpResponse

import pandas as pd
from io import BytesIO


def get_rendered_excel_file_response(pool: CommentPool, comment_list):
    output_file_name: str = generate_output_file_name(pool.id, "xlsx")

    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df = pd.DataFrame([comment.get_as_json() for comment in comment_list])
        df.to_excel(writer, sheet_name='slug')
        writer.close()
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % output_file_name
        return response
