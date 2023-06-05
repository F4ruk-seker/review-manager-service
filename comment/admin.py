from django.contrib import admin
from comment import models


admin.site.register(models.CommentTag)
admin.site.register(models.CommentModel)
# Register your models here.
