from django.urls import path
from .views import (
    todo_detail, 
    todo_list, 
    todo_create, 
    todo_update, 
    todo_delete
) 

app_name = 'todos'

urlpatterns = [
    # path('', todo_list, name="home"), function url
    path('', todo_list.as_view(), name="home"), #class url

    # path('create/', todo_create), #function url
    path('create/', todo_create.as_view()),

    # path('<id>/', todo_detail), function url
    path('<str:pk>/', todo_detail.as_view()), #class url


    # path('<id>/update', todo_update),

    path('<id>/delete', todo_delete), 
    path('<str:pk>/update', todo_update.as_view(), name="update"), #class url
]