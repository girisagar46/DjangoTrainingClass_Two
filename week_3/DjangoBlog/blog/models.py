from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


# Our cusotm model managers
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset()\
                                          .filter(status='published')\
                                          .order_by('-created')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    author = models.ForeignKey("auth.User", related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # managers
    objects = models.Manager()
    published = PublishManager() # use our custom model manager

    # Meta information
    class Meta:
        ordering = ('-publish',) # sort by publish date in the admin view

    # String representation
    def __str__(self):
        return self.title


class Comment(models.Model):
    post_id = models.ForeignKey('Post', related_name='post_comments', on_delete=CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    comment_body = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.name} in ({self.post_id.title})" # For Py3.6 +