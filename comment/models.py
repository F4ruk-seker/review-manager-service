from django.db import models
from django.core.exceptions import ValidationError


class CommentModel(models.Model):
    text = models.TextField()
    ai_tag = models.ForeignKey('CommentTag', on_delete=models.SET_NULL, null=True, blank=True,
                               help_text="tagged from ai service", related_name="ai_tag")
    tag = models.ForeignKey('CommentTag', on_delete=models.SET_NULL, null=True, blank=True,related_name="human_tag")
    branch_from = models.ForeignKey('branch.BranchModel', on_delete=models.SET_NULL, null=True, blank=True)

    def get_as_json(self) -> dict:
        return {
            'text': self.text,
            'ai_tag': self.ai_tag.name if self.ai_tag else None,
            'tag': self.tag.name if self.tag else None,
        }


class CommentTag(models.Model):
    name = models.TextField()
    explanation = models.TextField()
    color = models.TextField(default=None, null=True)

    @classmethod
    def load_built_in_tags(cls) -> None:
        tags = [
            {"name": "YETKİNLİK", "explanation": "Açıklama yok"},
            {"name": "İÇTEN", "explanation": "Açıklama yok"},
            {"name": "SAYGIN", "explanation": "Açıklama yok"},
            {"name": "GÜÇLÜ", "explanation": "Açıklama yok"},
            {"name": "HEYCAN", "explanation": "Açıklama yok"},
            {"name": "OLUMSUZ", "explanation": "Açıklama yok"},
        ]
        for tag in tags:
            cls.objects.create(
                name=tag.get('name'),
                explanation=tag.get('explanation')
            )

    def __str__(self):
        return f"{ self.name } - { self.explanation }"





    '''
    
    def save(
        self, *args, **kwargs
    ):
        if not self.is_trained:
            return super().save(self, *args, **kwargs)
        else:
            raise ValidationError('you cannot update if your repository is trained')
            
    '''
