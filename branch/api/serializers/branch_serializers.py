from rest_framework import serializers
from branch.models import BranchModel


class BranchSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=True)
    url = serializers.URLField(required=True)
    explanation = serializers.CharField(required=False)

    class Meta:
        model = BranchModel
        # fields = '__all__'
        exclude = ('metric', )
        lookup_field = 'id'

