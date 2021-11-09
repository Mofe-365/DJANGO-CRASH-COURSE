from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from .models import Todo
from .form import TodoForm, userform

from django.views import generic

# def todo_list(request):
#     todos = Todo.objects.all()
#     print(todos)
#     context = {
#         "todo_list": todos
#     }
#     return render(request, "todo/todo_list_inner.html", context)

# classbase version of todo_list
# class todo_list(generic.TemplateView):
#     template_name = "todo/todo_list_inner.html"

class todo_list(generic.ListView):
    template_name = 'todo/todo_list_inner.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        queryset = Todo.objects.all()
        return queryset

# def todo_detail(request, id):
#     todo = Todo.objects.get(id=id)
#     context = {
#         "todo" : todo
#     }
#     return render(request, "todo/todo_detail.html", context)

class todo_detail(generic.DetailView):
    template_name = 'todo/todo_detail.html'
    queryset = Todo.objects.all()
    context_object_name = "todo"


# def todo_create(request):
#     form = TodoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#         # print(form.cleaned_data)
#         pass
#     context = {
#         "form" : form
#     }
#     return render(request, "todo/todo_create.html", context)

class todo_create(generic.CreateView):
    template_name = 'todo/todo_create.html'
    form_class = TodoForm

    def get_success_url(self):
        return reverse("todo:home")


# def todo_update(request, id):
#     todo = Todo.objects.get(id=id)
#     form = TodoForm(request.POST or None, instance=todo)
#     if form.is_valid():
#         form.save()
#         return redirect('/')

#     context = { "form": form }
#     return render(request, "todo/todo_update.html", context)

class todo_update(generic.UpdateView):
    template_name = 'todo/todo_update.html'
    form_class = TodoForm
    queryset = Todo.objects.all()

    def get_success_url(self):
        return reverse("todos:home")

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('/')

class signupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = userform

    def get_success_url(self):
        return reverse("login")