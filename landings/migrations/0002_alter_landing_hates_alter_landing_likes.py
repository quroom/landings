# Generated by Django 4.1.1 on 2022-10-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landing",
            name="hates",
            field=models.IntegerField(blank=True, null=True, verbose_name="hates"),
        ),
        migrations.AlterField(
            model_name="landing",
            name="likes",
            field=models.IntegerField(blank=True, null=True, verbose_name="likes"),
        ),
    ]
