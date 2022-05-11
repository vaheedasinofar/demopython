from django.urls import path

from todoapp import views

app_name = 'todoapp'
urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:taskid>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('dbvhome/<int:pk>/',views.Taskdetailview.as_view(),name='dbvhome'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
]
