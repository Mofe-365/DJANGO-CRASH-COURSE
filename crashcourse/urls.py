from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from todo.views import signupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('todo.urls', namespace='todos'))
]
