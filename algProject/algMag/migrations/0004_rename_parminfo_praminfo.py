# Generated by Django 4.2.15 on 2024-08-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("algMag", "0003_alter_alginfo_prams"),
    ]

    operations = [
        migrations.RenameModel(old_name="ParmInfo", new_name="PramInfo",),
    ]