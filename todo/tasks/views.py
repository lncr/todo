from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    @action(methods=['post', ], detail=True)
    def finished(self, request, pk=None):
        task = self.get_object()
        task.is_finished = not task.is_finished
        task.save()
        serializer = self.get_serializer(instance=task)
        return Response(serializer.data)
