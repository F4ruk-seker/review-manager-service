from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from comment.api.serializers import CommentSerializer
from comment.models import CommentModel, CommentTag


class CommentCreateView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)

    @staticmethod
    def validate(attrs):
        text = attrs.get('text')
        existing_branches = CommentModel.objects.filter(text=text)
        if existing_branches.exists():
            raise ValidationError("Bu url e sahip bir şube zaten mevcut.")
        return attrs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.validate(serializer.validated_data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
