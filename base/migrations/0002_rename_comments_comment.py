# Generated by Django 4.2.2 on 2023-06-27 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
