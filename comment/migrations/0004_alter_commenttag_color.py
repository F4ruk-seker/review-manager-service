# Generated by Django 4.2.1 on 2023-07-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_commenttagcolor_commenttag_sub_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttag',
            name='color',
            field=models.TextField(),
        ),
    ]