from rest_framework import serializers
from branch.models import BranchModel, BranchMetric


class BranchMetricSerializer(serializers.ModelSerializer):

    def get_metric_chart(self, *args, **kwargs):
        context = []

        label = []
        color = []
        value = []
        model: BranchMetric = args[0]
        metrics = model.get_metric()
        data = {}
        for metric in metrics:
            data[metric.get('name')] = metric.get('result')
        return data

    class Meta:
        model = BranchMetric
        fields = '__all__'

    calculation_time = serializers.DateField(read_only=True, required=False)
    chart_context = serializers.SerializerMethodField(method_name='get_metric_chart')


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


