# Generated by Django 4.1 on 2022-09-17 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_training_topics_alter_quizquestion_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='training',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
