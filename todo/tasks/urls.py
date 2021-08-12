from django.urls import path
from rest_framework.routers import SimpleRouter

from tasks.views import TaskView

router = SimpleRouter()
router.register('tasks', TaskView)
urlpatterns = []

urlpatterns += router.urls
