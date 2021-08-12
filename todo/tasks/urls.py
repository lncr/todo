from django.urls import path

from tasks.views import TaskListView, TaskDetailGenericView, SetFinishedTaskAPIView, TaskCreateView, \
    TaskUpdateGenericView, TaskDestroyGenericView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/creation/', TaskCreateView.as_view()),
    path('tasks/<int:id>/', TaskDetailGenericView.as_view()),
    path('tasks/<int:id>/update/', TaskUpdateGenericView.as_view()),
    path('tasks/<int:id>/delete/', TaskDestroyGenericView.as_view()),
    path('tasks/<int:id>/finished/', SetFinishedTaskAPIView.as_view()),
]
