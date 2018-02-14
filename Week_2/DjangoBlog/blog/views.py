from django.shortcuts import render

from blog.models import Post


def home(request):
    object_list = Post.objects.order_by("-created_date")
    count = object_list.count()
    ctx = {
        "object_list": object_list,
        "count": count
    }
    return render(request, 'home.html', context=ctx)

def about(request):
    return render(request, 'about.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
