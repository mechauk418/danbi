# Generated by Django 4.1 on 2023-04-30 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_alter_task_subtask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='SubTask',
        ),
        migrations.AddField(
            model_name='subtask',
            name='Task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='Todo.task'),
        ),
    ]