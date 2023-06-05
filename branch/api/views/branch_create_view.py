from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status
from branch.models import BranchModel
from branch.api.serializers import BranchSerializer


class BranchCreateView(CreateAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer

    @staticmethod
    def validate(attrs):
        url = attrs.get('url')
        existing_branches = BranchModel.objects.filter(url=url)
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
