# Generated by Django 4.0.4 on 2022-04-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_customuser_alter_answer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='tags',
            field=models.ManyToManyField(null=True, to='app.tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(null=True, to='app.tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(null=True),
        ),
    ]