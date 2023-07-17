from django.contrib import admin
from comment import models
from django.utils.html import format_html


admin.site.register(models.CommentTag)
admin.site.register(models.CommentModel)


class CommentTagColorModelAdmin(admin.ModelAdmin):
    list_display = ('colored_test_field',)  # Add any other fields you want to display

    def colored_test_field(self, obj):
        return format_html("@ {2} > <span style='color:#{0};'>{1}</span>", obj.hex_code, obj, obj.name)

    colored_test_field.short_description = 'Colored Test Field'


admin.site.register(models.CommentTagColor, CommentTagColorModelAdmin)

# Register your models here.
