from django.urls import path
from rest_framework.routers import SimpleRouter

from tasks.views import SetFinishedTaskAPIView, TaskView

router = SimpleRouter()
router.register('tasks', TaskView)
urlpatterns = [
    path('tasks/<int:id>/finished/', SetFinishedTaskAPIView.as_view()),
]

urlpatterns += router.urls
