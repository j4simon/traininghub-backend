# Generated by Django 4.1 on 2022-09-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_quizquestion_topic_remove_training_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='training',
            name='topics',
        ),
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='title', max_length=50),
        ),
        migrations.AddField(
            model_name='training',
            name='title',
            field=models.CharField(default='title', max_length=25),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=15),
        ),
    ]