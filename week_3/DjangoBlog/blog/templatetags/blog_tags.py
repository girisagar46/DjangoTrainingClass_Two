from datetime import datetime

from django import template
from django.db.models import Q

from DjangoBlog.settings import BLOG_NAME

from blog.models import Post

register = template.Library()


# 1. Simple Tag
@register.simple_tag
def blog_name():
    return BLOG_NAME

@register.simple_tag
def count():
    return Post.published.all().count()

@register.simple_tag
def footer():
    year = datetime.today().year
    return "Copyright {}".format(str(year))

@register.simple_tag
def current_time():
    return datetime.now().date()


# 2. Inclusion Tag
@register.inclusion_tag('blog/latest.html')
def get_latest(count=None):
    latest = []
    if count is not None:
        latest = Post.published.all()[:count]
    else:
        latest = Post.published.all()[:4]
    return {"latest_blogs":latest}


# 3. Assignment Tag
@register.assignment_tag
def similars(title, q_pk):
    similar = Post.published.filter(
                        Q(title__contains=title) | Q(body__contains=title)
                    ).exclude(pk=q_pk)
    return similar


# 4. Custom Filters
@register.filter
def capitalize_title(title):
    return title.upper()

