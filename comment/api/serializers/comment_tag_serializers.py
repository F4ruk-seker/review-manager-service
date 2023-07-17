from rest_framework import serializers
from comment.models import CommentTag
from comment.api.serializers.comment_tag_color import CommentTagColorSerializer


class CommentTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentTag
        # fields = ('id', 'name')
        fields = '__all__'

    color = CommentTagColorSerializer()
