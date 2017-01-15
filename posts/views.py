from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
    context = {
        "title": "create"
    }
    return render(request, "index.html", context)

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

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
