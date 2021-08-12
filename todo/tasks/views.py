from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views, generics
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TaskDetailGenericView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskUpdateGenericView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskDestroyGenericView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Task.objects.all()
    lookup_field = 'id'


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
