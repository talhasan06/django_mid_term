
from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_tasks,name="show_tasks"),
    path('add/',views.add_task,name="add_task"),
    path('edit/<int:id>',views.edit_task,name="edit_task"),
    path('delete/<int:id>',views.delete_task,name="delete_task"),
]
