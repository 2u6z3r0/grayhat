from django.conf.urls import url
from .views import (post_delete, post_create,
                    post_details, post_list,
                    post_update)

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^create$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_details, name="details"),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete$', post_delete),

]