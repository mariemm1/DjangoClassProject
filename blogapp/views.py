from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from blogapp.forms import BlogForm
from blogapp.models import BlogPost

class BlogView(ListView):
    model=BlogPost
    context_object_name='posts'
    template_name="Posts/blogView.html"




class BlogCreateWithFields(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author', 'created_on']
    template_name = "Posts/blogcreate.html"
    success_url = reverse_lazy('Posts:listhtml')


class BlogCreateWithForm(CreateView):
    model = BlogPost
    form_class = BlogForm
    template_name = "Posts/blogcreateForm.html"
    success_url = reverse_lazy('Posts:listhtml')


class blogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'content',]
    pk_url_kwarg = 'id'
    template_name = "Posts/blogUpdate.html"
    success_url = reverse_lazy('Posts:listhtml')

class blogDeleteView(DeleteView):
    model = BlogPost
    pk_url_kwarg = 'id'
    template_name = "Posts/blogdelete.html"
    success_url = reverse_lazy('Posts:listhtml')