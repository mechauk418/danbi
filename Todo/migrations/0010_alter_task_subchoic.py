# Generated by Django 4.1 on 2023-05-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0009_alter_task_subchoic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subchoic',
            field=models.JSONField(blank=True, null=True),
        ),
    ]