# Generated by Django 4.2.1 on 2023-07-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_branchmetric_negative_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchmetric',
            name='calculation_time',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]
