from django.urls import path 
from . import views

urlpatterns = [
    path('',views.entry,name="entry"),
    path('home/',views.tasklist,name="tasklist"),
    path('view-task/<int:taskid>/',views.viewtask, name="viewtask"),
    path('create-task/',views.createtask,name="createtask"),
    path('delete-task/<int:taskid>',views.deletetask,name="deletetask"),
    path('update-task/<int:taskid>',views.updatetask,name="updatetask"),
    path('register-user',views.register,name="register"),
    path('sign-in',views.signin,name="signin"),
    path('sign-out',views.signout,name="signout")
]