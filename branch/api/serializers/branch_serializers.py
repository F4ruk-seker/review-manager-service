from rest_framework import serializers
from branch.models import BranchModel


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchModel
        # fields = '__all__'
        exclude = ('metric', )
