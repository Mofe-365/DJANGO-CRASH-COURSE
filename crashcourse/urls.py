from django.contrib import admin
from django.urls import path, include

from todo.views import signupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupView.as_view(), name='signup'),
    path('', include('todo.urls', namespace='todos'))
]
