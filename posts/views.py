from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        messages.success(request, "post created")
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Create Post",
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_details(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_details.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "object_list": queryset
    }
    return render(request, 'index.html', context)

def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        messages.success(request, "Post updated")
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Edit Post",
        "form": form
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post deleted")
    return redirect("posts:list")
