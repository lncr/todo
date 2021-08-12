from rest_framework import serializers
from django.contrib.auth import get_user_model

from tasks.models import Task


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', ]


class TaskSerializer(serializers.ModelSerializer):

    estimated_finish_time = serializers.DateTimeField(format='%d:%m:%Y %H:%M', input_formats=['%d:%m:%Y %H:%M', ])
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'owner', 'body', 'estimated_finish_time', 'is_finished', ]
        read_only_fields = ['is_finished', ]
