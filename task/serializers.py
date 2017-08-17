from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'created_by'

        )


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'tasks',)
