from django.http import HttpResponse
from xml.etree.ElementTree import Element, ElementTree

from .output_file_name import generate_output_file_name

from ai.models import CommentPool
from comment.models import CommentModel


def get_rendered_xml_file_response(pool: CommentPool, comment_list):
    root = Element('comments')
    output_file_name: str = generate_output_file_name(pool.id, "xml")

    for comment in comment_list:
        comment_element = Element('comment')
        for key, value in comment.get_as_json().items():
            child_element = Element(key)
            child_element.text = str(value)
            comment_element.append(child_element)

        root.append(comment_element)

    tree = ElementTree(root)
    response = HttpResponse(content_type='application/xml')
    response['Content-Disposition'] = f'attachment; filename="{output_file_name}"'
    tree.write(response, encoding='utf-8')

    return response
