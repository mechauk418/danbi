from django.db import models

# Create your models here.

team_list = (
        ('단비','단비'),
        ('다래','다래'),
        ('블라블라','블라블라'),
        ('철로','철로'),
        ('땅이','땅이'),
        ('해태','해태'),
        ('수피','수피'),
    )

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    create_user = models.CharField(max_length=80)
    team = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=80)
    is_complete = models.BooleanField(default=False)
    compleated_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    modified_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    subchoic = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.CharField(null=True, blank=True,max_length=80,choices=team_list)
    is_complete = models.BooleanField(default=False)
    compleated_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    modified_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    task = models.ForeignKey(Task,null=False,blank=False, related_name='subtasks', on_delete=models.CASCADE)


