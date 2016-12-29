from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Post, Category
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category']


def index(request):
    categories = Category.objects.order_by('-name')[:5]
    post_list = {}
    for c in categories:
        post_list[c.name] = Post.objects.filter(category=c)
    context = {
        'post_list': post_list.items(),
    }
    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})


def post_create(request, template_name='posts/post_form.html'):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('blog:index')
    return render(request, template_name, {'form': form})


def post_update(request, pk, template_name='posts/post_form.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog:index')
    return render(request, template_name, {'form': form})


def post_delete(request, pk, template_name='posts/post_confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, template_name, {'object': post})
