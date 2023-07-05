from ai.models import CommentPool
from rest_framework import serializers
from comment.api.serializers import CommentSerializer, CustomizedCommentBranchSerializer
from branch.models import BranchModel


class PoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentPool
        # fields = '__all__'
        exclude = ('comments', )


class PoolCommentSerializer(serializers.ModelSerializer):
    comments = CustomizedCommentBranchSerializer(many=True)

    class Meta:
        model = CommentPool
        fields = '__all__'
