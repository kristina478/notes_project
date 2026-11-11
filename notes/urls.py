from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.note_create, name="create"),
    path("<int:pk>/edit/", views.note_update, name="update"),
    path("<int:pk>/delete/", views.note_delete, name="delete"),
]