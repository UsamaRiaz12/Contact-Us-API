# Generated by Django 4.1.5 on 2023-07-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("em_register", "0003_em_register_resume"),
    ]

    operations = [
        migrations.AddField(
            model_name="em_register",
            name="name2",
            field=models.CharField(default="Unknown", max_length=255),
        ),
    ]