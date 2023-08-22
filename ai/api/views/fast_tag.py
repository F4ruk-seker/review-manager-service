from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

from ai.api.serializers import CommentTagSerializer
from comment.models import CommentModel


class ListAsQuerySet(list):

    def __init__(self, *args, model, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return self  # filter ignoring, but you can impl custom filter

    def order_by(self, *args, **kwargs):
        return self


class FastTagPagination(PageNumberPagination):
    page_size = 1


class FastTag(ListCreateAPIView):
    pagination_class = FastTagPagination
    serializer_class = CommentTagSerializer

    def get_queryset(self) -> ListAsQuerySet:
        _: list = []  # temp
        for comment in CommentModel.objects.filter(tag=None).order_by('id'):
            if not comment.is_time_out_range():
                _.append(comment)

        return ListAsQuerySet(_, model=CommentModel)


