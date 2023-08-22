from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()


class Operation(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.TextField(default=None, null=True)
    branch = models.ManyToManyField('branch.BranchModel')
    defined_ai = models.ForeignKey('ai.AIManager', on_delete=models.CASCADE)
