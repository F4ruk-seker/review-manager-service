from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timezone, timedelta


class CommentModel(models.Model):
    text = models.TextField()
    ai_tag = models.ForeignKey('CommentTag', on_delete=models.SET_NULL, null=True, blank=True,
                               help_text="tagged from ai service", related_name="ai_tag")
    tag = models.ForeignKey('CommentTag', on_delete=models.SET_NULL, null=True, blank=True,related_name="human_tag")
    branch_from = models.ForeignKey('branch.BranchModel', on_delete=models.SET_NULL, null=True, blank=True)
    create = models.DateTimeField(auto_created=True, default=None, null=True)

    pass_time_out = models.DateTimeField(default=None, null=True, blank=True)

    def is_time_out_range(self):
        if self.pass_time_out is not None:
            end_time = self.pass_time_out.replace(tzinfo=timezone.utc)
            current_time = datetime.now(timezone.utc)
            return not current_time > end_time

        else:
            return False

    def get_as_json(self):
        return {
            'text': self.text,
            'ai_tag': self.ai_tag.name if self.ai_tag else None,
            'tag': self.tag.name if self.tag else None,
        }


# sincere_count = models.IntegerField(default=0)
# reputable_count = models.IntegerField(default=0)
# powerful_count = models.IntegerField(default=0)
# competence_count = models.IntegerField(default=0)
# excitement_count = models.IntegerField(default=0)


class CommentTag(models.Model):
    name = models.TextField()
    sub_name = models.TextField(default=None, null=True)
    explanation = models.TextField()
    color = models.ForeignKey('comment.CommentTagColor',default=None, null=True, blank=True, on_delete=models.CASCADE)

    @classmethod
    def load_built_in_tags(cls):
        tags = [
            {"name": "YETKİNLİK", 'sub_name': 'competence', "explanation": "Açıklama yok"},
            {"name": "İÇTEN", 'sub_name': 'sincere', "explanation": "Açıklama yok"},
            {"name": "SAYGIN", 'sub_name': 'reputable', "explanation": "Açıklama yok"},
            {"name": "GÜÇLÜ", 'sub_name': 'powerful', "explanation": "Açıklama yok"},
            {"name": "HEYCAN", 'sub_name': 'excitement', "explanation": "Açıklama yok"},
            {"name": "OLUMSUZ", 'sub_name': 'negative', "explanation": "Açıklama yok"},
        ]
        for tag in tags:
            cls.objects.create(
                name=tag.get('name'),
                sub_name=tag.get('sub_name'),
                explanation=tag.get('explanation')
            )

    def __str__(self):
        return f"{ self.name } - { self.explanation }"


class CommentTagColor(models.Model):
    name = models.TextField()
    hex_code = models.TextField()

    def __str__(self):
        return f"{self.name.title()} #{self.hex_code}"

