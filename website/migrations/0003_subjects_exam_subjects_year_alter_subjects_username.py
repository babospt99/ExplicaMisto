# Generated by Django 5.0 on 2023-12-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_rename_name_subjects_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="subjects",
            name="exam",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subjects",
            name="year",
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name="subjects",
            name="username",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]