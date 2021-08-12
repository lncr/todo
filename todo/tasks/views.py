from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views, viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class SetFinishedTaskAPIView(views.APIView):

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        if task.is_finished:
            task.is_finished = False
        else:
            task.is_finished = True
        task.save()
        serializer = TaskSerializer(instance=task)
        return Response(serializer.data)
