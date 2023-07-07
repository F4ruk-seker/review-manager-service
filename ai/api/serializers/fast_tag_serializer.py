from comment.models import CommentModel
from rest_framework import serializers
from comment.api.serializers import CommentSerializer, CustomizedCommentBranchSerializer
from branch.models import BranchModel


class CommentTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        # fields = '__all__'
        exclude = ('branch_from', )
