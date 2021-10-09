from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from . models import Blog
from . models import Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . forms import CommentForm
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def blog_home(request):
    context = {}
    post = Blog.objects.all()
    context['post'] = post
    return render(request, 'blog_home.html', context)

@login_required(login_url='/login/')
def blog_detail(request, pk):
    user = request.user
    context = {}
    try:
        data = Blog.objects.get(id=pk)
        comments = Comment.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exit")
    form = CommentForm(request.POST)
    if form.is_valid():
        text = Comment(comment=form.cleaned_data['comment'], author=user, blog=data)
        text.save()
        return redirect(f'/blog/{pk}')
    else:
        form = CommentForm()

    context['data'] = data
    context['comments'] = comments
    context['form'] = form
    return render(request, 'blog_detail.html', context)

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ('title','description', 'body', 'post_image', 'author',)
    success_url = reverse_lazy('blog_home')
    LOGIN_URL = 'login'

    def form_valid(self, form): 
          form.instance.author = self.request.user
          return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = '__all__'
    succress_url = reverse_lazy('blog_home')
    LOGIN_URL = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.author)
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_home')
    LOGIN_URL = 'login'

    def dispatch(self, request, *args, **kwargs):
          obj = self.get_object()
          if obj.author != self.request.user:
               raise PermissionDenied
          return super().dispatch(request, *args, **kwargs)
