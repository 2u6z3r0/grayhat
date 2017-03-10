from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Post(models.Model):
    title = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:details", kwargs={"slug": self.slug})
        # return "/post/%s" % self.id

    def get_markdown(self):
        content = self.content
        return mark_safe(markdown(content))

    class Meta:
        ordering = ["-created", "-updated"]
    objects = PostManager()


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_post_signal_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_post_signal_receiver, sender=Post)