from rest_framework import serializers
from comment.models import CommentModel
from .comment_tag_serializers import CommentTagSerializer


class CommentSerializer(serializers.ModelSerializer):
    ai_tag = CommentTagSerializer()
    tag = CommentTagSerializer()

    class Meta:
        model = CommentModel
        fields = '__all__'
