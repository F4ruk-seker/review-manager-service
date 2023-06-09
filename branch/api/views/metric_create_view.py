from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status
from branch.models import BranchMetric
from branch.api.serializers import BranchMetricSerializer


class BranchMetricCreateView(CreateAPIView):
    queryset = BranchMetric.objects.all()
    serializer_class = BranchMetricSerializer


