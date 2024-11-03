# Generated by Django 4.2.1 on 2023-07-26 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ai', '0004_alter_aimanager_trained_structure'),
        ('branch', '0005_alter_branchmetric_calculation_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None, null=True)),
                ('branch', models.ManyToManyField(to='branch.branchmodel')),
                ('defined_ai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai.aimanager')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]