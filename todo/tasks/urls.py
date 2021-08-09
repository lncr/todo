from django.urls import path

from tasks.views import TaskAPIView


urlpatterns = [
    path('tasks/', TaskAPIView.as_view())
]
