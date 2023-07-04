from rest_framework import serializers

from ai.models import CommentTag


class CommentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTag
        fields = ('name', )
