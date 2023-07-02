from rest_framework import serializers
from comment.models import CommentTag


class CommentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTag
        fields = ('id', 'name')

