from django.urls import path
from . views import index,add_todo,edit,delete,completes,compltete_one,delete_all

app_name="todos"

urlpatterns=[
    path("",index,name="home"),
    path("add/",add_todo,name="add"),
    path("completed/",compltete_one,name="completeone"),
    path("delete-all/",delete_all,name="completedelete"),
    path("edits/<pk>/",edit,name="edt"),
    path("delete-data/<pk>/",delete,name="delte"),
    path("complete-data/<pk>/",completes,name="complete"),
    
]