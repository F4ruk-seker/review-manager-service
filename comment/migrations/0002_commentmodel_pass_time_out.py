# Generated by Django 4.2.1 on 2023-07-12 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='pass_time_out',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
