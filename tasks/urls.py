from django.urls import URLPattern, path
from . import views
import tasks

app_name="tasks"
urlpatterns=[
    path("", views.index, name="index"),
    path("add", views.add,name="add")
]