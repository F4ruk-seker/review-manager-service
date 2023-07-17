from rest_framework import serializers
from branch.models import BranchModel, BranchMetric


class BranchMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchMetric
        fields = '__all__'

    calculation_time = serializers.DateField(read_only=True)


class BranchSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=True)
    url = serializers.URLField(required=True)
    explanation = serializers.CharField(required=False)
    metric_list = serializers.SerializerMethodField()

    @staticmethod
    def get_metric_list(obj) :
        metric_list: list = []
        for metric in obj.get_metrics():
            metric_list.append(
                BranchMetricSerializer(instance=metric).data
            )
        return metric_list

    # calculation_time

    class Meta:
        model = BranchModel
        # fields = '__all__'
        exclude = ('metric', )
        lookup_field = 'id'


