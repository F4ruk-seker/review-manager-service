# Generated by Django 4.2.1 on 2023-07-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtokenmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
