from django.db import models
from comment.models import CommentTag
import uuid


class AIManager(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.TextField()
    pool = models.ForeignKey('ai.CommentPool', editable=True, on_delete=models.CASCADE, null=True)
    trained_structure = models.FilePathField(path='/.trained_data', allow_files=['.sav'])


class CommentPool(models.Model):
    name = models.TextField()
    comments = models.ManyToManyField('comment.CommentModel')
    is_trained = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True, auto_created=True)

    def get_stats(self) -> dict:
        tag_list = CommentTag.objects.all().order_by('name')
        tag_list_dict: dict = {}

        for tag in tag_list:
            tag_list_dict[tag.name] = {'count': 0}

        for tag in tag_list:
            tag_list_dict[tag.name] = {'count': self.comments.filter(tag=tag).count()}

        tag_list_dict["unTAG"] = {'count': self.comments.filter(tag=None).count()}

        return tag_list_dict

    def get_colored_stats(self):
        tags = self.get_stats()
        colors = ['primary', 'success', 'danger', 'warning', 'info', 'light', 'secondary']
        for tag, color in zip(tags, colors):
            tags[tag]['color'] = color
        return tags

