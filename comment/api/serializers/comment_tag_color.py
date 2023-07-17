from rest_framework import serializers
from comment.models import CommentTagColor


class CommentTagColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTagColor
        # fields = ('id', 'name')
        fields = '__all__'

