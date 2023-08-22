from django.db import models
import uuid


class ScraperClient(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Task(models.Model):
    target_branch = models.ForeignKey('branch.BranchModel', on_delete=models.CASCADE, null=True)
    status = models.ForeignKey('scraper.Status', on_delete=models.CASCADE, null=True)
    scraper = models.ForeignKey('scraper.ScraperClient', on_delete=models.CASCADE, null=True)


class Status(models.Model):
    is_clean = models.BooleanField(default=False)  # when false > get er obj.
    is_success = models.BooleanField(default=False)

    end_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now=True)

    explanation = models.TextField()

    def __bool__(self):
        return self.is_success

