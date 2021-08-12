from rest_framework import status
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


class TaskDetailAPIView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            update_fields = []
            for field, value in serializer.validated_data.items():
                setattr(task, field, value)
                update_fields.append(field)
            task.save(update_fields=update_fields)

            serializer = TaskSerializer(instance=task)
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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
