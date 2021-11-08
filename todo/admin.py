from django.contrib import admin
from .models import Todo, personal_info

admin.site.register(Todo)
admin.site.register(personal_info)