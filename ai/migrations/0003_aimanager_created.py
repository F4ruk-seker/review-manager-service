# Generated by Django 4.2.1 on 2023-07-22 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0002_aimanager_trained_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimanager',
            name='created',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]