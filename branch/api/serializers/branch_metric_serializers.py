from rest_framework import serializers
from branch.models import BranchMetric


class BranchMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchMetric
        # fields = '__all__'
        exclude = ('calculation_time', )

