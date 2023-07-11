from django.db import models
from django.contrib.auth import get_user_model

import uuid
# Create your models here.
user = get_user_model()
from datetime import datetime, timezone, timedelta

# Assuming self.end_time is an offset-naive datetime object

# Assuming current_time is an offset-aware datetime object

class AuthTokenModel(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    token = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    start_time = models.DateTimeField(auto_created=True)
    end_time = models.DateTimeField(null=True, default=None, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.end_time = datetime.now() + timedelta(days=15)
        super().save(*args, **kwargs)

    def is_live(self):
        end_time = self.end_time.replace(tzinfo=timezone.utc)
        current_time = datetime.now(timezone.utc)

        return not current_time > end_time

    def __str__(self):
        return f"login_{self.user}_'{self.token}'> {self.end_time.strftime('%d-%m-%Y : %H:%M')}"
