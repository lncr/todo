from django.urls import path

from tasks.views import TaskListView, TaskDetailGenericView, SetFinishedTaskAPIView, TaskCreateView


urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/creation/', TaskCreateView.as_view()),
    path('tasks/<int:id>/', TaskDetailGenericView.as_view()),
    path('tasks/<int:id>/finished/', SetFinishedTaskAPIView.as_view()),
]
