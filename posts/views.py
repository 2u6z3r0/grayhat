from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
# from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.db.models import Q
# Create your views here.


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        messages.success(request, "post created")
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Create Post",
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_details(request, slug):
    today = timezone.now().date()
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    if not instance.draft:
        instance.total_views += 1
        instance.save()
    context = {
        "title": instance.title,
        "instance": instance,
        "today": today
    }
    return render(request, "post_details.html", context)


def post_list(request):
    queryset_list = Post.objects.active()
    queryset_top_list = Post.objects.active().order_by('-total_views')[:5]
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
        )

    paginator = Paginator(queryset_list, 8) #shows 8 posts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # if page number is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g 9999) deliver the last page
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "page_request_var": page_request_var,
        "top_post": queryset_top_list,
    }
    return render(request, 'post_list.html', context)


def post_update(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
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


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Post deleted")
    return redirect("posts:list")
