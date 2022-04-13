# Generated by Django 4.0.4 on 2022-04-13 14:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_answer_tags_alter_question_tags_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='avatar',
        ),
    ]