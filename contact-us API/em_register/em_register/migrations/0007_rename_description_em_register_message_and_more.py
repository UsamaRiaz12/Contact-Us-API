# Generated by Django 4.1.5 on 2023-09-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "em_register",
            "0006_em_register_email_alter_em_register_company_name_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="em_register",
            old_name="description",
            new_name="message",
        ),
        migrations.RenameField(
            model_name="em_register",
            old_name="company_name",
            new_name="your_email",
        ),
        migrations.RenameField(
            model_name="em_register",
            old_name="date",
            new_name="your_name",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="email",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="job_tittle",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="requirments",
        ),
        migrations.AddField(
            model_name="em_register",
            name="subject",
            field=models.TextField(default="", max_length=100),
        ),
    ]