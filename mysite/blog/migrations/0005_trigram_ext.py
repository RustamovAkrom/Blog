# Generated by Django 5.0.3 on 2024-08-15 10:12
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_publish_comment_active'),
    ]

    operations = [
        TrigramExtension()
    ]
