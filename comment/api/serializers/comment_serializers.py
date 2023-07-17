from rest_framework import serializers

from branch.models import BranchModel
from comment.models import CommentModel
from .comment_tag_serializers import CommentTagSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = '__all__'


class CommentPassSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = ('id', )


class CustomizedCommentBranchSerializer(CommentSerializer):
    ai_tag = CommentTagSerializer()
    tag = CommentTagSerializer()

    branch_from = serializers.SerializerMethodField(method_name='get_branch')

    @staticmethod
    def get_branch(comment_obj):

        return {
            'id': comment_obj.branch_from.id if comment_obj.branch_from else None,
            'name': comment_obj.branch_from.name if comment_obj.branch_from else None
        }
