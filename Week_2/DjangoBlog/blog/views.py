from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from blog.models import Post


# def home(request):
#     object_list = Post.objects.order_by("-created_date")
#     count = object_list.count()
#     ctx = {
#         "object_list": object_list,
#         "count": count
#     }
#     return render(request, 'home.html', context=ctx)


def get_one_post(request, *args, **kwargs):
    arg = kwargs.get('pk')
    # one_post = Post.objects.get(pk=arg)
    one_post = get_object_or_404(Post, pk=arg)
    ctx = {
        "one_post": one_post
    }
    return render(request, 'post_detail.html', context=ctx)



# def about(request):
#     return render(request, 'about.html', context={})

# def contact(request):
#     return render(request, 'contact.html', context={})


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        object_list = Post.objects.order_by("-created_date")
        count = object_list.count()
        ctx = {
            "object_list": object_list,
            "count": count,
        }
        return render(request, 'home.html', context=ctx)


class ContactView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', context={})


class PostListView(ListView):
    model = Post
    template_name = 'home.html'









