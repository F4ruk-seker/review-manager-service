# Generated by Django 4.2.1 on 2023-07-01 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aimanager',
            name='trained_structure',
            field=models.FileField(default=None, null=True, upload_to='D:\\.trained_data'),
        ),
    ]