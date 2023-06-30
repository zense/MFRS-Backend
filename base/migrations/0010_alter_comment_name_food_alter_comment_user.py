# Generated by Django 4.2.2 on 2023-06-28 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0009_alter_comment_name_food_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name_food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.food'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
