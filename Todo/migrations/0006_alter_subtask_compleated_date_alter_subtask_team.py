# Generated by Django 4.1 on 2023-05-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_remove_subtask_task_subtask_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='compleated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='team',
            field=models.CharField(blank=True, choices=[('단비', '단비'), ('다래', '다래'), ('블라블라', '블라블라'), ('철로', '철로'), ('땅이', '땅이'), ('해태', '해태'), ('수피', '수피')], max_length=80, null=True),
        ),
    ]
