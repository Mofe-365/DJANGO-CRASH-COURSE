from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from .models import Todo
from .form import TodoForm, userform

from django.views import generic

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list_inner.html", context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo" : todo
    }
    return render(request, "todo/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
        # print(form.cleaned_data)
        pass
    context = {
        "form" : form
    }
    return render(request, "todo/todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = { "form": form }
    return render(request, "todo/todo_update.html", context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('/')

class signupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = userform

    def get_success_url(self):
        return reverse("todos:home")