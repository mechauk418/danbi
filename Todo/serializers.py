from rest_framework import serializers, fields
from .models import *

class SubTaskSerializer(serializers.ModelSerializer):

    task = serializers.ReadOnlyField(source="task.id")
    
    class Meta:
        model = SubTask
        fields = [
            'id',
            'team',
            'is_complete',
            'compleated_date',
            'task'
        ]


team_list = (
        ('단비','단비'),
        ('다래','다래'),
        ('블라블라','블라블라'),
        ('철로','철로'),
        ('땅이','땅이'),
        ('해태','해태'),
        ('수피','수피'),
        ('test11','test11'),
    )

class TaskSerializer(serializers.ModelSerializer):

    test = serializers.SerializerMethodField()
    subchoic = serializers.MultipleChoiceField(choices = team_list)
    def get_test(self,obj):
        tes = obj.subtasks.all()
        return SubTaskSerializer(instance=tes, many=True, context = self.context).data

    class Meta:
        model = Task
        fields = [
            'id',
            'create_user',
            'team',
            'title',
            'content',
            'is_complete',
            'compleated_date',
            'test',
            'subchoic'
        ]

    def create(self, validated_data):
        instance = Task.objects.create(**validated_data)
        ch_list = self.context['request'].data.getlist('subchoic')
        for team in ch_list:
            print(team)
            SubTask.objects.create(team=team, task =instance)

        return instance