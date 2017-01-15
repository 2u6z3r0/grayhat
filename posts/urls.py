from django.conf.urls import url
from .views import (post_delete, post_create,
                    post_details, post_list,
                    post_update)

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create$', post_create),
    url(r'^(?P<id>\d+)/$', post_details, name="details"),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^delete$', post_delete),

]