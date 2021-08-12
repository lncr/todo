from django.urls import path

from tasks.views import TaskListView, TaskDetailAPIView, SetFinishedTaskAPIView, TaskCreateView


urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/creation/', TaskCreateView.as_view()),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view()),
    path('tasks/<int:id>/finished/', SetFinishedTaskAPIView.as_view()),
]
