from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, QuerySet
from branch.models import BranchModel
from branch.api.serializers import BranchSerializer
from comment.models import CommentModel
from comment.api.serializers import CommentSerializer


class CommentUpdateDestroyRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('name', 'id', 'url')
    # search_fields = ('name', 'id', 'url')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(args)
        print(kwargs.items())
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

