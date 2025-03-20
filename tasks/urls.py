from django.urls import path
from . import views

app_name='tasks'

urlpatterns = [
    path('',views.tasks_view,name='view'),
    path('<slug:slug>',views.task_page,name='page'),
    path('add/',views.task_add,name='add'),
    path('update/<int:pk>/',views.task_update,name='update'),
    path('delete/<int:pk>/',views.task_delete,name='delete'),
    path('complete/<int:pk>/',views.task_complete,name='complete'),
]